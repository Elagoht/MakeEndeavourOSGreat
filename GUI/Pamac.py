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
                               "Pamac is a graphical software manager/application market created by Manjaro team. It makes installing, updating and removing apps easy.",
                               self, self.parent().parent().barBottom)
        # Create AUR section
        self.gbxAUR = \
            ButtonBox("AUR Support for Pamac",
                      "Assets/Apps/aur.png",
                      "Arch User Repository is an additional package source. It's necessery for lots of package and application (like Spotify, Discord etc.). But be careful when installing unknown packages. Noone can guarantee that all of AUR packages is up to date and safe. You can use it but do not install packages you don't know or trust!", (
                          CommandButton(QIcon("Assets/enabled.png"), "Enable AUR",
                                        "sudo sed -Ei '/EnableAUR/s/^#//' /etc/pamac.conf",
                                        self),
                          CommandButton(QIcon("Assets/disabled.png"), "Disable AUR",
                                        "sudo sed -Ei '/EnableAUR/s/^/#/' /etc/pamac.conf",
                                        self))
                      )

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.appPamac)
        self.layout.addWidget(self.gbxAUR)
        self.layout.addStretch()
