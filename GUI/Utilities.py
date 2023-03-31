from os import popen
from Result import CommandButton
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QGroupBox, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


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


class AppBox(QGroupBox):
    def __init__(self, title: str, package: str, image: str, description: str = ""):
        super(QGroupBox, self).__init__()
        self.glyApp = QVBoxLayout(self)
        self.layInfo = QHBoxLayout()
        self.layButtons = QHBoxLayout()

        self.lblTitle = QLabel(title)
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
        self.setTitle(title)
        self.glyExt = QHBoxLayout(self)

        self.imgExt = QLabel(self)
        self.imgExt.setPixmap(QPixmap(image))
        self.imgExt.setFixedWidth(36)
        self.lblExt = QLabel(f"<a href=\"{link}\">Visit Page</a>")
        self.lblExt.setWordWrap(True)
        self.lblExt.setOpenExternalLinks(True)
        self.lblExt.setTextFormat(Qt.RichText)
        self.lblExt.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.glyExt.addWidget(self.imgExt)
        self.glyExt.addWidget(self.lblExt)
