from os import popen, system, WEXITSTATUS
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QGroupBox, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QThread, QProcess, pyqtSignal
from typing import Iterable
from json import load


class CommandButton(QPushButton):
    # Create a button to run commands in a separated thread
    def __init__(self, icon: QIcon, text: str, command: str, parent: QWidget) -> None:
        super(QPushButton, self).__init__()
        self.setParent(parent)
        self.text = text
        self.setText(self.text)
        self.setIcon(icon)
        self.thread = CommandThread(command)
        self.clicked.connect(self.thread.start)
        self.thread.output.connect(self.on_thread_output)

    def set_status(self, status_code) -> None:
        status_icon = ""
        match status_code:
            case 0:
                self.setStyleSheet("color: green")
                status_icon = "✓"
            case -1:
                self.setStyleSheet("color: gray")
                status_icon = "☠"
            case _:
                self.setStyleSheet("color: red")
                status_icon = "✗"
        self.setText(f"{self.text} {status_icon}")

    def on_thread_output(self, status_code) -> None:
        self.set_status(status_code)


class CommandThread(QThread):
    # Create thread worker for command button.
    output = pyqtSignal(int)

    def __init__(self, command) -> None:
        super().__init__()
        self.command = command

    def run(self) -> None:
        process = QProcess()
        process.start("bash")
        process.write(f"""statusfile=$(mktemp);
        xterm -bg black -fg green -e sh -c '{self.command}; echo $? > '$statusfile 2> /dev/null;
        cat $statusfile;
        rm $statusfile""".encode())
        process.closeWriteChannel()
        process.waitForFinished()

        status_code = process.readAllStandardOutput()\
            .data().decode()
        if status_code != "":
            status_code = status_code.splitlines()[-1]
        try:
            status_code = int(status_code)
        except ValueError:
            status_code = -1
        self.output.emit(status_code)


class AppBox(QGroupBox):
    def __init__(self, title: str, package: str, image: str, description: str) -> None:
        super(QGroupBox, self).__init__()
        self.glyApp = QVBoxLayout(self)
        self.layButtons = QHBoxLayout()

        self.lblTitle = QLabel("<b>" + title + "<b>")
        self.lblDescription = QLabel(
            f"""
            <table style="float: left;">
                <tr>
                    <td width="136" height="136"> <!-- Placing table because Qt supports float only for images and tables -->
                        <img src="{image}" />
                    </td>
                </tr>
            </table>
            <span>
                {description}
            </span>""")
        self.lblDescription.setOpenExternalLinks(True)
        self.lblDescription.setTextFormat(Qt.RichText)
        self.lblDescription.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.lblDescription.setWordWrap(True)
        self.btnInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install",
            install_if_doesnt_have(package), self)
        self.btnUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall",
            uninstall_if_have(package), self)

        self.layButtons.addWidget(self.btnInstall)
        self.layButtons.addWidget(self.btnUninstall)
        self.glyApp.addWidget(self.lblTitle)
        self.glyApp.addWidget(self.lblDescription)
        self.glyApp.addStretch()
        self.glyApp.addLayout(self.layButtons)
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")


class ButtonBox(QGroupBox):
    def __init__(self, title: str, image: str, description: str, buttons: Iterable[QPushButton]) -> None:
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
        # for button, function in zip(buttons, functions):
        #     button.clicked.connect(
        #         (lambda _button, _function: (
        #             lambda: run_command(_function, _button))
        #          )(button, function)
        #     )
        #     self.layButtons.addWidget(button)
        for button in buttons:
            self.layButtons.addWidget(button)
        self.glyApp.addWidget(self.lblTitle)
        self.glyApp.addLayout(self.layInfo)
        self.glyApp.addLayout(self.layButtons)
        self.setStyleSheet("""QGroupBox {
            background: rgba(0, 0, 0, .25);
            border: 1px solid rgba(0, 0, 0, .5);
            border-radius: .25em;
        }""")


class GridBox(QGroupBox):
    def __init__(self, title: str) -> None:
        super(QGroupBox, self).__init__()
        self.setTitle(title)
        self.glyField = QGridLayout(self)

    def addWidget(self, widget: QWidget, row: int = 0, col: int = 0, rSpan: int = 1, cSpan: int = 1) -> None:
        self.glyField.addWidget(widget, row, col, rSpan, cSpan)
        for column in range(self.glyField.columnCount()):
            self.glyField.setColumnStretch(column, 1)

    def addWidgets(self, *widgets: QWidget) -> None:
        for widget in widgets:
            self.glyField.addWidget(widget)
        for column in range(self.glyField.columnCount()):
            self.glyField.setColumnStretch(column, 1)


class ExtensionBox(QGroupBox):
    def __init__(self, title: str, link: str, image: str) -> None:
        super(QGroupBox, self).__init__()
        self.glyExt = QHBoxLayout(self)

        self.imgExt = QLabel(self)
        self.imgExt.setPixmap(QPixmap(image))
        self.imgExt.setFixedWidth(36)
        self.lblExt = QLabel(
            f"< a href=\"{link}\" style=\"text-decoration: none; color:cornflowerblue\">{title}</a>")
        self.lblExt.setWordWrap(True)
        self.lblExt.setOpenExternalLinks(True)
        self.lblExt.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.glyExt.addWidget(self.imgExt)
        self.glyExt.addWidget(self.lblExt)
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")


class ThemeBox(QGroupBox):
    def __init__(self, name: str, package: str, image: str, themes: dict, type: int = 0) -> None:
        """
        type 0 = GTK Theme
        type 1 = Icon Theme
        type 2 = Cursor Theme
        """
        match type:
            case 1:
                self.to_change = "icon-theme"
            case 2:
                self.to_change = "cursor-theme"
            case _:
                self.to_change = "gtk-theme"

        super(QGroupBox, self).__init__()
        self.glyTheme = QVBoxLayout(self)
        self.layInfo = QGridLayout()
        self.layButtons = QGridLayout()

        self.lblThemeTitle = QLabel("<b>" + name + "</b>", self)
        self.lblThemeTitle.setWordWrap(True)
        self.imgTheme = QLabel(self)
        self.imgTheme.setPixmap(QPixmap(image))
        self.imgTheme.setFixedSize(128, 128)

        self.btnThemeInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install",
            install_if_doesnt_have(package),
            self
        )
        self.btnThemeUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"),
            "Uninstall",
            uninstall_if_have(package),
            self
        )
        self.layInfo.addWidget(self.imgTheme, 0, 0, 3, 1)
        self.layInfo.addWidget(self.lblThemeTitle, 0, 1)
        self.layInfo.addWidget(self.btnThemeInstall, 1, 1)
        self.layInfo.addWidget(self.btnThemeUninstall, 2, 1)
        self.glyTheme.addLayout(self.layInfo)
        self.glyTheme.addLayout(self.layButtons)
        self.glyTheme.addStretch()

        # Bundle buttons and functions
        self.buttons = [CommandButton(
            QIcon("GUI/Assets/configure.png"), name,
            f"""[ "$(pacman -Qqs {package} | grep ^{package}$)" = "{package}" ] && \
            gsettings set org.gnome.desktop.interface {self.to_change} '{theme}'""",
            self)
            for name, theme in themes.items()
        ]
        # self.functions = [
        #     f"""[ "$(pacman -Qqs {package} | grep ^{package}$)" = "{package}" ] && gsettings set org.gnome.desktop.interface {self.to_change} '{theme}'"""
        #     for theme in themes.values()
        # ]

        # for number, (button, function) in enumerate(zip(self.buttons, self.functions)):
        #     button.clicked.connect(
        #         (lambda _button, _function: (
        #             lambda: run_command(_function, _button))
        #          )(button, function)
        #     )
        for number, button in enumerate(self.buttons):
            if number == 1:
                self.layButtons.addWidget(button, 0, 1)
            else:
                self.layButtons.addWidget(button)

        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")

    def set_this(self, theme_string: str, package: str, result_widget: CommandButton) -> None:
        if WEXITSTATUS(system(f"[ ! \"$(pacman -Qqs {package} | grep \"^{package}$\")\" = \"{package}\" ]")) == 0:
            result_widget.set_status(-1)
            return
        run_command(f"gsettings set org.gnome.desktop.interface \"{theme_string}\"",
                    result_widget)


class FontBox(QGroupBox):
    def __init__(self, name: str, package: str) -> None:
        super(QGroupBox, self).__init__()
        self.glyFont = QGridLayout(self)
        self.lblFontTitle = QLabel("<b>" + name + "</b>", self)
        self.lblFontTitle.setWordWrap(True)
        self.btnFontInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install", install_if_doesnt_have(package), self)
        self.btnFontUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall", uninstall_if_have(package), self)
        self.btnFontSet = CommandButton(
            QIcon("GUI/Assets/enabled.png"), "Select", self.set_this(name, package), self)
        self.glyFont.addWidget(self.lblFontTitle, 0, 0, 1, 2)
        self.glyFont.addWidget(self.btnFontInstall, 1, 0, 1, 1)
        self.glyFont.addWidget(self.btnFontUninstall, 1, 1, 1, 1)
        self.glyFont.addWidget(self.btnFontSet, 2, 0, 1, 2)
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")

    def set_this(self, font_family: str, package: str) -> None:
        if WEXITSTATUS(system(f"[ ! \"$(pacman -Qqs {package} | grep \"^{package}$\")\" = \"{package}\" ]")) == 0:
            return "false"
        font_size = popen(
            "gsettings get org.gnome.desktop.interface monospace-font-name")\
            .readline().strip().split()[-1].replace("'", "")
        return f"gsettings set org.gnome.desktop.interface monospace-font-name \"{font_family} {font_size}\""


class ShellBox(AppBox):
    def __init__(self, title: str, package: str, image: str, description: str, uninstallable: bool = False) -> None:
        super().__init__(title, package, image, description)

        # If uninstallable remove install buttons
        if uninstallable:
            self.glyApp.removeWidget(self.btnInstall)
            self.glyApp.removeWidget(self.btnUninstall)
            del self.btnInstall
            del self.btnUninstall

        # Setter buttons
        self.btnSet = CommandButton(
            QIcon("GUI/Assets/configure.png"), "Set Default",
            f"echo New shell will be {package}.;\
                [ \"{package}\" = \"sh\" ] || [ \"$(pacman -Qqs {package} | grep ^{package}$)\" = \"{package}\" ] &&\
                chsh -s /bin/{package}",
            self)
        self.btnSetRoot = CommandButton(
            QIcon("GUI/Assets/configure.png"), "Set Default for Root", f"echo New shell will be {package}.; [ \"$(pacman -Qqs {package} | grep ^{package}$)\" = \"{package}\" ] && sudo chsh -s /bin/{package} root", self)

        # Add buttons to layout
        self.laySetButtons = QHBoxLayout()
        self.laySetButtons.addWidget(self.btnSet)
        self.laySetButtons.addWidget(self.btnSetRoot)
        self.glyApp.addLayout(self.laySetButtons)


class AppsTab(QWidget):
    def __init__(self, json_file: str) -> None:
        super(QWidget, self).__init__()

        self.layout = QVBoxLayout(self)
        with open(json_file, "r") as programs_json:
            program_lists = load(programs_json)
        for language_name, program_list in program_lists.items():
            grid_box = GridBox(language_name)
            for number, program in enumerate(program_list):
                match number:
                    case 1:
                        grid_box.addWidget(AppBox(*program), 0, 1)
                    case 2:
                        grid_box.addWidget(AppBox(*program), 0, 2)
                    case _:
                        grid_box.glyField.addWidget(AppBox(*program))
            self.layout.addWidget(grid_box)


class MonoFont(QFont):
    def __init__(self) -> None:
        super(QFont, self).__init__("Monospace")
        self.setPointSize(12)
        self.setStyleHint(QFont.Monospace)


class CommandLine(QTextEdit):
    def __init__(self, text, height) -> None:
        super(QTextEdit, self).__init__()
        self.setText(text)
        self.setFont(MonoFont())
        self.setFixedHeight(height)
        self.setReadOnly(True)
        self.setStyleSheet(
            """QTextEdit {
                background: black;
            }""")


def run_command(command: str, result_widget: CommandButton) -> None:
    thrTerm = QThread()
    thrTerm.finished.connect(thrTerm.terminate)
    result = popen(f"""statusfile=$(mktemp);
        xterm -bg black -fg green -e sh -c '{command}; echo $? > '$statusfile 2> /dev/null;
        cat $statusfile;
        rm $statusfile
""").readline()
    if result == "":
        result = -1
    result_widget.set_status(int(result))


def aur_helper() -> str:
    return popen("""if [ -f /bin/paru ]; then
    aurhelper="/bin/paru"
elif [ -f /bin/yay ]; then
    aurhelper="/bin/yay"
else
    aurhelper=""
fi
echo $aurhelper""").readline().strip()


def has_aur_helper() -> bool:
    return aur_helper() != ""


def install_if_doesnt_have(package: str) -> str:
    return f"""if [ ! "$(pacman -Qqs {package} | grep "^{package}$")" = "{package}" ]
    then {aur_helper()} -S {package}
fi""" if has_aur_helper() else "false"


def uninstall_if_have(package: str) -> str:
    return f"""if [ "$(pacman -Qqs {package} | grep "^{package}$" )" = "{package}" ]
    then {aur_helper()} -R {package}
fi""" if has_aur_helper() else "false"


def color(color: str, text: str) -> str:
    return f"<font color='{color}'>{text}</font>"
