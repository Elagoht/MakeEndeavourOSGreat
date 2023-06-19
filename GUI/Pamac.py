from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from Utilities import ButtonBox, AppBox, CommandButton, get_installed_apps


class PamacWin(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)

        # Create install section
        self.installed_apps = get_installed_apps()
        self.appPamac = AppBox("Install Pamac", "pamac-aur", "Assets/Apps/pamac.png",
                               "Pamac is a graphical software manager and application market developed by the Manjaro team. It simplifies the process of installing, updating, and removing applications, providing a user-friendly interface for these tasks.",
                               self, self.parent().parent().barBottom)
        # Create AUR section
        self.gbxAUR = \
            ButtonBox("AUR Support for Pamac",
                      "Assets/Apps/aur.png",
                      "The Arch User Repository (AUR) is an extra source of packages for Arch Linux. It is often needed for installing applications like Spotify and Discord. However, it is important to be cautious when using the AUR. Not all packages in the AUR are regularly updated or guaranteed to be safe. Only install packages from the AUR that you know and trust.", (
                          CommandButton(QIcon("Assets/enabled.png"), "Enable AUR",
                                        "pkexec sed -Ei '/EnableAUR/s/^#//' /etc/pamac.conf",
                                        self, avoid_xterm=True),
                          CommandButton(QIcon("Assets/disabled.png"), "Disable AUR",
                                        "pkexec sed -Ei '/EnableAUR/s/^/#/' /etc/pamac.conf",
                                        self, avoid_xterm=True))
                      )

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.appPamac)
        self.layout.addWidget(self.gbxAUR)
        self.layout.addStretch()
