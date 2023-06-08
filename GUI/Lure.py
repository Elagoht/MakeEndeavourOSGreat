from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from Utilities import AppBox, GridBox, color, CommandLine, get_installed_apps


class LureWin(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.installed_apps = get_installed_apps()
        self.gbxLure = AppBox("Linux User Repository", "linux-user-repository-bin", "Assets/Apps/lure.png",
                              "LURE allows users to install software that may not be widely distributed through official repositories, while still maintaining the convenience of installation through repository sources. This includes features such as updates and simple uninstallation. Additionally, LURE provides developers with a central location for all their users to use to install their software.",
                              self, self.parent().parent().barBottom)

        self.gbxUsage = GridBox("Usage of LURE")
        self.lblUsage = QLabel(
            "You can use LURE by following commands:", self.gbxUsage)
        self.cmdUsage = CommandLine(
            "<div>" +
            color("green", "lure ") +
            color("yellow", "install ") +
            color("orange", "package_name ") +
            color("gray", "# Installs specified package.") + "</div><div>" +
            color("green", "lure ") +
            color("yellow", "remove ") +
            color("orange", "package_name ") +
            color("gray", "# Uninstalls specified package.") + "</div><div>" +
            color("green", "lure ") +
            color("yellow", "refresh ") +
            color("gray", "# Refresh database.") + "</div><div>" +
            color("green", "lure ") +
            color("yellow", "upgrade ") +
            color("gray", "# Upgrades all available packages.") + "</div><div>" +
            color("green", "lure ") +
            color("yellow", "list ") +
            color("gray", "# Lists all packages in repository.") + "</div><div>" +
            color("green", "lure ") +
            color("yellow", "help ") +
            color("gray", "# Prints detailed help page.") +
            "</div>",
            150
        )
        self.gbxUsage.addWidgets(self.lblUsage, self.cmdUsage)

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxLure)
        self.layout.addWidget(self.gbxUsage)
