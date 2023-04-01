from PyQt5.QtWidgets import QWidget, QGroupBox, QPushButton, QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from Result import CommandButton
from os import popen
from Utilities import run_command, GridBox, ButtonBox


class AurHelperTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create description section
        self.gbxAur = GridBox("What is AUR Helper")
        self.lblAurDesc = QLabel("Arch User Repository packages needs to be install manually by cloning git repositories (technically downloading files from internet but in a cooler way), and running some commands that creating packages from recipe file. That's usually a few step process. In this point, AUR helpers helps you to install, update and uninstall packages from AUR and official repositories.")
        self.lblAurDesc.setWordWrap(True)
        self.btnAurCheck = CommandButton(
            QIcon("GUI/Assets/check.png"), "Check AUR Helpers", self.gbxAur)
        self.lblAurHelper = QLabel(self.gbxAur)
        self.gbxAur.addWidget(self.lblAurDesc)
        self.gbxAur.addWidget(self.btnAurCheck, 1, 0)
        self.gbxAur.addWidget(self.lblAurHelper, 2, 0)

        # Create paru section
        self.appParu = ButtonBox("Paru", "", "Paru is most popular AUR helper written in rust.", (
            CommandButton(QIcon("GUI/Assets/install.png"),
                          "Install", self),
            CommandButton(QIcon("GUI/Assets/uninstall.png"),
                          "Uninstall", self)
        ), (
            """if [ ! -f /bin/paru ]
                then workdir=$(mktemp -d) &&
                cd $workdir &&
                git clone https://aur.archlinux.org/paru-bin.git &&
                cd paru-bin &&
                makepkg -si &&
                rm -rf $workdir
            fi""",
            """if [ -f /bin/paru ]
                then sudo pacman -R paru-bin || sudo pacman -R paru
            fi"""
        ))

        # Create yay section
        self.gbxYay = QGroupBox("Yay", self)
        self.glyYay = QGridLayout(self.gbxYay)
        self.lblYay = QLabel(
            "Yay is widely used AUR helper written in go.")
        self.lblYay.setWordWrap(True)
        self.btnYayInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxYay)
        self.btnYayUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall", self.gbxYay)
        self.glyYay.addWidget(self.lblYay, 0, 0, 1, 2)
        self.glyYay.addWidget(self.btnYayInstall, 1, 0)
        self.glyYay.addWidget(self.btnYayUninstall, 1, 1)

        # Connect buttons to functions
        self.btnAurCheck.clicked.connect(
            lambda: self.lblAurHelper.setText(self.get_aur_helpers()))
        self.btnYayInstall.clicked.connect(lambda: run_command(
            """if [ ! -f /bin/yay ]
    then workdir=$(mktemp -d) &&
    cd $workdir &&
    git clone https://aur.archlinux.org/yay-bin.git &&
    cd yay-bin &&
    makepkg -si &&
    rm -rf $workdir
fi""", self.btnYayInstall))  # Installing AUR helper without an AUR helper.
        self.btnYayUninstall.clicked.connect(lambda: run_command(
            """if [ -f /bin/yay ]
    then sudo pacman -R yay-bin || sudo pacman -R yay
fi""", self.btnYayUninstall))

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxAur)
        self.layout.addWidget(self.appParu)
        self.layout.addWidget(self.gbxYay)

        # Initialize
        self.lblAurHelper.setText(self.get_aur_helpers())

    def has_paru(self):
        return popen("pacman -Qqs paru")\
            .readline().strip() in ("paru", "paru-bin")

    def has_yay(self):
        return popen("pacman -Qqs yay")\
            .readline().strip() in ("yay", "yay-bin")

    def get_aur_helpers(self):
        helpers = []
        if self.has_paru():
            helpers.append("paru")
        if self.has_yay():
            helpers.append("yay")
        return f"Your installed AUR helper{'s' if len(helpers) > 1 else ''}: "\
            + ", ".join(helpers) + "."\
            if len(helpers) else "You do not have any AUR helper."
