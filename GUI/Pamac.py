from PyQt5.QtWidgets import QWidget, QGroupBox, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from Result import CommandButton
from Utilities import aur_helper, has_aur_helper, run_command


class PamacTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create install section
        self.gbxPamac = QGroupBox("Install Pamac", self)
        self.glyPamac = QVBoxLayout(self.gbxPamac)
        self.lblPamac = QLabel(
            "Pamac is a graphical software manager/application market created by Manjaro team. It makes installing, updating and removing apps easy.",
            self.gbxPamac)
        self.lblPamac.setWordWrap(True)
        self.btnInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxPamac)
        self.btnUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall", self.gbxPamac)
        self.glyPamac.addWidget(self.lblPamac)
        self.glyPamac.addWidget(self.btnInstall)
        self.glyPamac.addWidget(self.btnUninstall)

        # Create AUR section
        self.gbxAUR = QGroupBox("AUR Support for Pamac", self)
        self.glyAUR = QVBoxLayout(self.gbxAUR)
        self.lblAUR = QLabel("Arch User Repository is an additional package source. It's necessery for lots of package and application (like Spotify, Discord etc.). But be careful when installing unknown packages. Noone can guarantee that all of AUR packages is up to date and safe. You can use it but do not install packages you don't know or trust!")
        self.lblAUR.setWordWrap(True)
        self.btnEnable = CommandButton(
            QIcon("GUI/Assets/enabled.png"), "Enable AUR", self.gbxAUR)
        self.btnDisable = CommandButton(
            QIcon("GUI/Assets/disabled.png"), "Disable AUR", self.gbxAUR)
        self.glyAUR.addWidget(self.lblAUR)
        self.glyAUR.addWidget(self.btnEnable)
        self.glyAUR.addWidget(self.btnDisable)

        # Connect buttons to functions
        self.btnInstall.clicked.connect(lambda: run_command(
            f"""if [ ! "$(pacman -Qq pamac-aur)" = "pamac-aur" ]
    then {aur_helper()} -S pamac-aur
fi""" if has_aur_helper() else "false",
            self.btnInstall))
        self.btnUninstall.clicked.connect(lambda: run_command(
            f"""if [ "$(pacman -Qq pamac-aur)" = "pamac-aur" ]
    then {aur_helper()} -R pamac-aur
fi""" if has_aur_helper() else "false",
            self.btnUninstall))
        self.btnEnable.clicked.connect(lambda: run_command(
            "sudo sed -Ei '/EnableAUR/s/^#//' /etc/pamac.conf",
            self.btnEnable))
        self.btnDisable.clicked.connect(lambda: run_command(
            "sudo sed -Ei '/EnableAUR/s/^/#/' /etc/pamac.conf",
            self.btnDisable))

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxPamac)
        self.layout.addWidget(self.gbxAUR)
