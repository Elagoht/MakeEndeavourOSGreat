from PyQt5.QtWidgets import QWidget, QGroupBox, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from Result import CommandButton
from Utilities import run_command, GridBox, AppBox


class PamacTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create install section
        self.appPamac = AppBox("Install Pamac", "pamac-aur", "GUI/Assets/Apps/pamac.png",
                               "Pamac is a graphical software manager/application market created by Manjaro team. It makes installing, updating and removing apps easy.")
        # Create AUR section
        self.gbxAUR = GridBox("AUR Support for Pamac")
        self.lblAUR = QLabel("Arch User Repository is an additional package source. It's necessery for lots of package and application (like Spotify, Discord etc.). But be careful when installing unknown packages. Noone can guarantee that all of AUR packages is up to date and safe. You can use it but do not install packages you don't know or trust!")
        self.lblAUR.setWordWrap(True)
        self.btnEnable = CommandButton(
            QIcon("GUI/Assets/enabled.png"), "Enable AUR", self.gbxAUR)
        self.btnDisable = CommandButton(
            QIcon("GUI/Assets/disabled.png"), "Disable AUR", self.gbxAUR)
        self.gbxAUR.addWidget(self.lblAUR, 0, 0, 1, 2)
        self.gbxAUR.addWidget(self.btnEnable, 1, 0)
        self.gbxAUR.addWidget(self.btnDisable, 1, 1)

        # Connect buttons to functions
        self.btnEnable.clicked.connect(lambda: run_command(
            "sudo sed -Ei '/EnableAUR/s/^#//' /etc/pamac.conf",
            self.btnEnable))
        self.btnDisable.clicked.connect(lambda: run_command(
            "sudo sed -Ei '/EnableAUR/s/^/#/' /etc/pamac.conf",
            self.btnDisable))

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.appPamac)
        self.layout.addWidget(self.gbxAUR)
