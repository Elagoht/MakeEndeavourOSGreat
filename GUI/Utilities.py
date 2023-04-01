from os import popen, system, WEXITSTATUS
from Result import CommandButton
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QGroupBox, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt
from typing import Iterable


def run_command(command: str, result_widget: CommandButton):
    result = popen(f"""statusfile=$(mktemp);
        xterm -bg black -fg green -e sh -c '{command}; echo $? > '$statusfile 2> /dev/null;
        cat $statusfile;
        rm $statusfile
""").readline()
    if result == "":
        result = -1
    result_widget.setStatus(int(result))


def aur_helper():
    return popen("""if [ -f /bin/paru ]; then
    aurhelper="/bin/paru"
elif [ -f /bin/yay ]; then
    aurhelper="/bin/yay"
else
    aurhelper=""
fi
echo $aurhelper""").readline().strip()


def has_aur_helper():
    return aur_helper() != ""


def install_if_doesnt_have(package: str, result_widget: CommandButton):
    run_command(
        f"""if [ ! "$(pacman -Qqs {package} | grep "^{package}$")" = "{package}" ]
    then {aur_helper()} -S {package}
fi""" if has_aur_helper() else "false", result_widget)


def uninstall_if_have(package: str, result_widget: CommandButton):
    run_command(
        f"""if [ "$(pacman -Qqs {package} | grep "^{package}$" )" = "{package}" ]
    then {aur_helper()} -R {package}
fi""" if has_aur_helper() else "false", result_widget)


def color(color: str, text: str) -> str:
    return f"<font color='{color}'>{text}</font>"


class AppBox(QGroupBox):
    def __init__(self, title: str, package: str, image: str, description: str = ""):
        super(QGroupBox, self).__init__()
        self.glyApp = QVBoxLayout(self)
        self.layInfo = QHBoxLayout()
        self.layButtons = QHBoxLayout()

        self.lblTitle = QLabel("<b>" + title + "<b>")
        self.imgApp = QLabel(self)
        self.imgApp.setPixmap(QPixmap(image))
        self.imgApp.setFixedSize(128, 128)
        self.lblDescription = QLabel(description)
        self.lblDescription.setWordWrap(True)
        self.btnInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install", self)
        self.btnUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall", self)

        self.layInfo.addWidget(self.imgApp)
        self.layInfo.addWidget(self.lblDescription)
        self.layButtons.addWidget(self.btnInstall)
        self.layButtons.addWidget(self.btnUninstall)
        self.glyApp.addWidget(self.lblTitle)
        self.glyApp.addLayout(self.layInfo)
        self.glyApp.addLayout(self.layButtons)
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")

        # Connect buttons to functions
        self.btnInstall.clicked.connect(
            lambda: install_if_doesnt_have(package, self.btnInstall))
        self.btnUninstall.clicked.connect(
            lambda: uninstall_if_have(package, self.btnUninstall))


class ButtonBox(QGroupBox):
    def __init__(self, title: str, image: str, description: str, buttons: Iterable[QPushButton], functions: Iterable[str]):
        super(QGroupBox, self).__init__()
        self.glyApp = QVBoxLayout(self)
        self.layInfo = QHBoxLayout()
        self.layButtons = QHBoxLayout()

        self.lblTitle = QLabel("<b>" + title + "<b>")
        self.imgApp = QLabel(self)
        self.imgApp.setPixmap(QPixmap(image))
        self.imgApp.setFixedSize(128, 128)
        self.lblDescription = QLabel(description)
        self.lblDescription.setWordWrap(True)

        self.layInfo.addWidget(self.imgApp)
        self.layInfo.addWidget(self.lblDescription)
        for button, function in zip(buttons, functions):
            button.clicked.connect(
                (lambda _button, _function: (
                    lambda: run_command(_function, _button))
                 )(button, function)
            )
            self.layButtons.addWidget(button)
        self.glyApp.addWidget(self.lblTitle)
        self.glyApp.addLayout(self.layInfo)
        self.glyApp.addLayout(self.layButtons)
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")


class GridBox(QGroupBox):
    def __init__(self, title: str):
        super(QGroupBox, self).__init__()
        self.setTitle(title)
        self.glyField = QGridLayout(self)

    def addWidget(self, widget: QWidget, row: int = 0, col: int = 0, rSpan: int = 1, cSpan: int = 1):
        self.glyField.addWidget(widget, row, col, rSpan, cSpan)

    def addWidgets(self, *widgets: QWidget):
        for widget in widgets:
            self.glyField.addWidget(widget)


class ExtensionBox(QGroupBox):
    def __init__(self, title: str, link: str, image: str):
        super(QGroupBox, self).__init__()
        self.glyExt = QHBoxLayout(self)

        self.imgExt = QLabel(self)
        self.imgExt.setPixmap(QPixmap(image))
        self.imgExt.setFixedWidth(36)
        self.lblExt = QLabel(
            f"< a href=\"{link}\" style=\"text-decoration: none; color:cornflowerblue\">{title}</a>")
        self.lblExt.setWordWrap(True)
        self.lblExt.setOpenExternalLinks(True)
        self.lblExt.setTextFormat(Qt.RichText)
        self.lblExt.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.glyExt.addWidget(self.imgExt)
        self.glyExt.addWidget(self.lblExt)
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")


class ThemeBox(QGroupBox):
    def __init__(self, name: str, package: str, themes: dict):
        super(QGroupBox, self).__init__()
        self.glyTheme = QGridLayout(self)
        self.lblThemeTitle = QLabel("<b>" + name + "</b>", self)
        self.lblThemeTitle.setWordWrap(True)
        self.btnThemeInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install", self)
        self.btnThemeUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall", self)
        self.glyTheme.addWidget(self.lblThemeTitle, 0, 0, 1, 2)
        self.glyTheme.addWidget(self.btnThemeInstall, 1, 0, 1, 1)
        self.glyTheme.addWidget(self.btnThemeUninstall, 1, 1, 1, 1)

        self.buttons = [CommandButton(
            QIcon("GUI/Assets/configure.png"), name, self)
            for name in themes.keys()
        ]
        self.functions = [
            f"gsettings set org.gnome.desktop.interface gtk-theme '{theme}'"
            for theme in themes.values()
        ]

        for button, function in zip(self.buttons, self.functions):
            button.clicked.connect(
                (lambda _button, _function: (
                    lambda: run_command(_function, _button))
                 )(button, function)
            )
            self.glyTheme.addWidget(button)

        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")

        # Connect buttons to functions
        self.btnThemeInstall.clicked.connect(
            lambda: install_if_doesnt_have(package, self.btnThemeInstall))
        self.btnThemeUninstall.clicked.connect(
            lambda: uninstall_if_have(package, self.btnThemeUninstall))

    def set_this(self, theme_string: str, package: str, result_widget: CommandButton) -> None:
        if WEXITSTATUS(system(f"[ ! \"$(pacman -Qqs {package} | grep \"^{package}$\")\" = \"{package}\" ]")) == 0:
            result_widget.setStatus(-1)
            return
        run_command(f"gsettings set org.gnome.desktop.interface \"{theme_string}\"",
                    result_widget)


class FontBox(QGroupBox):
    def __init__(self, name: str, package: str):
        super(QGroupBox, self).__init__()
        self.glyFont = QGridLayout(self)
        self.lblFontTitle = QLabel("<b>" + name + "</b>", self)
        self.lblFontTitle.setWordWrap(True)
        self.btnFontInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install", self)
        self.btnFontUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall", self)
        self.btnFontSet = CommandButton(
            QIcon("GUI/Assets/enabled.png"), "Select", self)
        self.glyFont.addWidget(self.lblFontTitle, 0, 0, 1, 2)
        self.glyFont.addWidget(self.btnFontInstall, 1, 0, 1, 1)
        self.glyFont.addWidget(self.btnFontUninstall, 1, 1, 1, 1)
        self.glyFont.addWidget(self.btnFontSet, 2, 0, 1, 2)
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")

        # Connect buttons to functions
        self.btnFontInstall.clicked.connect(
            lambda: install_if_doesnt_have(package, self.btnFontInstall))
        self.btnFontUninstall.clicked.connect(
            lambda: uninstall_if_have(package, self.btnFontUninstall))
        self.btnFontSet.clicked.connect(
            lambda: self.set_this(name, package, self.btnFontSet))

    def set_this(self, font_family: str, package: str, result_widget: CommandButton) -> None:
        if WEXITSTATUS(system(f"[ ! \"$(pacman -Qqs {package} | grep \"^{package}$\")\" = \"{package}\" ]")) == 0:
            result_widget.setStatus(-1)
            return
        font_size = popen(
            "gsettings get org.gnome.desktop.interface monospace-font-name")\
            .readline().strip().split()[-1].replace("'", "")
        run_command(f"gsettings set org.gnome.desktop.interface monospace-font-name \"{font_family} {font_size}\"",
                    result_widget)


class MonoFont(QFont):
    def __init__(self):
        super(QFont, self).__init__("Monospace")
        self.setPointSize(12)
        self.setStyleHint(QFont.Monospace)


class CommandLine(QTextEdit):
    def __init__(self, text, height):
        super(QTextEdit, self).__init__()
        self.setText(text)
        self.setFont(MonoFont())
        self.setFixedHeight(height)
        self.setReadOnly(True)
