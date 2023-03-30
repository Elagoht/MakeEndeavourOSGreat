from os import popen
from Result import ResultWidget
from PyQt5.QtWidgets import QGridLayout, QGroupBox, QPushButton, QWidget
from PyQt5.QtGui import QIcon


def run_command(command: str, result_widget: ResultWidget):
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


def install_if_doesnt_have(package: str, result_widget: ResultWidget):
    run_command(
        f"""if [ ! "$(pacman -Qqs {package} | grep "^{package}$")" = "{package}" ]
    then {aur_helper()} -S {package}
fi""" if has_aur_helper() else "false", result_widget)


def uninstall_if_have(package: str, result_widget: ResultWidget):
    run_command(
        f"""if [ "$(pacman -Qqs {package} | grep "^{package}$" )" = "{package}" ]
    then {aur_helper()} -R {package}
fi""" if has_aur_helper() else "false", result_widget)


class AppBox(QGroupBox):
    def __init__(self, title: str, package: str):
        super(QGroupBox, self).__init__()
        self.setTitle(title)
        self.glyApp = QGridLayout(self)
        # self.imgApp = QPixmap(image,"")
        self.btnInstall = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install", self)
        self.resInstall = ResultWidget()
        self.btnUninstall = QPushButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall", self)
        self.resUninstall = ResultWidget()
        # self.glyApp.addWidget(self.imgApp, 0, 0, 1, 2)
        self.glyApp.addWidget(self.btnInstall, 1, 0)
        self.glyApp.addWidget(self.btnUninstall, 1, 1)
        self.glyApp.addWidget(self.resInstall, 2, 0)
        self.glyApp.addWidget(self.resUninstall, 2, 1)

        # Connect buttons to functions
        self.btnInstall.clicked.connect(
            lambda: install_if_doesnt_have(package, self.resInstall))
        self.btnUninstall.clicked.connect(
            lambda: uninstall_if_have(package, self.resUninstall))


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
