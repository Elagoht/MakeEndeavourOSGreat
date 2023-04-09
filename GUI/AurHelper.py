from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QIcon
from os import popen
from Utilities import GridBox, ButtonBox, CommandButton


class AurHelperWin(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create description section
        self.gbxAur = GridBox("What is AUR Helper")
        self.lblAurDesc = QLabel("Arch User Repository packages needs to be install manually by cloning git repositories (technically downloading files from internet but in a cooler way), and running some commands that creating packages from recipe file. That's usually a few step process. In this point, AUR helpers helps you to install, update and uninstall packages from AUR and official repositories.")
        self.lblAurDesc.setWordWrap(True)
        self.btnAurCheck = CommandButton(
            QIcon("GUI/Assets/check.png"), "Check AUR Helpers", "true", self.gbxAur)
        self.btnAurCheck.clicked.connect(
            lambda: self.lblAurHelper.setText(self.get_aur_helpers()))
        self.lblAurHelper = QLabel(self.gbxAur)
        self.gbxAur.addWidget(self.lblAurDesc)
        self.gbxAur.addWidget(self.btnAurCheck, 1, 0)
        self.gbxAur.addWidget(self.lblAurHelper, 2, 0)

        # Create paru section
        self.appParu = \
            ButtonBox("Paru", "GUI/Assets/Apps/paru.png", "Paru is the most popular AUR helper written in Rust.", (
                CommandButton(QIcon("GUI/Assets/install.png"), "Install",
                              """if [ ! -f /bin/paru ]
                                then workdir=$(mktemp -d) &&
                                cd $workdir &&
                                git clone https://aur.archlinux.org/paru-bin.git &&
                                cd paru-bin &&
                                makepkg -si &&
                                rm -rf $workdir
                            fi""",
                              self, (lambda: self.lblAurHelper.setText(self.get_aur_helpers()),)),
                CommandButton(QIcon("GUI/Assets/uninstall.png"), "Uninstall",
                              """if [ -f /bin/paru ]
                                then sudo pacman -R paru-bin || sudo pacman -R paru
                              fi""",
                              self, (lambda: self.lblAurHelper.setText(self.get_aur_helpers()),)))
                      )

        # Create yay section
        self.appYay = \
            ButtonBox("Yay", "GUI/Assets/Apps/yay.png", "Yay is widely used AUR helper written in Go.", (
                CommandButton(QIcon("GUI/Assets/install.png"), "Install",
                              """if [ ! -f /bin/yay ]
                                then workdir=$(mktemp -d) &&
                                cd $workdir &&
                                git clone https://aur.archlinux.org/yay-bin.git &&
                                cd yay-bin &&
                                makepkg -si &&
                                rm -rf $workdir
                              fi""",
                              self, (lambda: self.lblAurHelper.setText(self.get_aur_helpers()),)),
                CommandButton(QIcon("GUI/Assets/uninstall.png"), "Uninstall",
                              """if [ -f /bin/yay ]
                                then sudo pacman -R yay-bin || sudo pacman -R yay
                              fi""",
                              self, (lambda: self.lblAurHelper.setText(self.get_aur_helpers()),))
            ))

        # Insert groupboxes to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.gbxAur, 0, 0, 1, 2)
        self.layout.addWidget(self.appParu)
        self.layout.addWidget(self.appYay)

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
        return f"Your installed AUR helper{'s' if len(helpers) > 1 else ''}: <font color=\"orange\">"\
            + " and ".join(helpers) + "</font>."\
            if len(helpers) else "<font color=\"red\">You do not have any AUR helper.</font>"
