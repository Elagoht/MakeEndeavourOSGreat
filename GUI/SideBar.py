from PyQt5.QtWidgets import QWidget, QVBoxLayout,  QPushButton
from PyQt5.QtGui import QIcon
from Utilities import AppsWin, CommandButton, has_aur_helper, aur_helper
from Gnome import GnomeWin
from Pamac import PamacWin
from AurHelper import AurHelperWin
from GnomeExtensions import ExtensionsWin
from Theming import AppearanceWin
from Lure import LureWin
from Shell import ShellWin
from Variables import VariableWin


class SideBar(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)

        # Declare AUR helper button text to safely edit it later
        self.txtAurButton = "AUR Helper"

        # Create window opener buttons
        self.btnUpdate = CommandButton(
            QIcon("Assets/upgrade.png"), "Update System",
            aur_helper()+" -Syu", self)
        self.btnAurHelper = QPushButton(self.txtAurButton)
        self.btnPamac = QPushButton("Software Manager")
        self.btnLure = QPushButton("LURE")
        self.btnEssentials = QPushButton("Essential Apps")
        self.btnGnome = QPushButton("Gnome Settings")
        self.btnExtension = QPushButton("Gnome Extensions")
        self.btnTheming = QPushButton("Appearance")
        self.btnVariables = QPushButton("Environment Variables")
        self.btnShell = QPushButton("Shell Program")
        self.btnGaming = QPushButton("Gaming Tools")
        self.btnGames = QPushButton("Recommended Games")
        self.btnDevelopment = QPushButton("Development")
        self.btnTerminalApp = QPushButton("Terminal Tools")

        # Insert buttons to menu layout
        self.layout = QVBoxLayout(self)
        self.layout.addStretch()
        self.layout.addWidget(self.btnUpdate)
        self.layout.addWidget(self.btnAurHelper)
        self.layout.addWidget(self.btnPamac)
        self.layout.addWidget(self.btnLure)
        self.layout.addWidget(self.btnGnome)
        self.layout.addWidget(self.btnExtension)
        self.layout.addWidget(self.btnTheming)
        self.layout.addWidget(self.btnVariables)
        self.layout.addWidget(self.btnShell)
        self.layout.addWidget(self.btnEssentials)
        self.layout.addWidget(self.btnGaming)
        self.layout.addWidget(self.btnGames)
        self.layout.addWidget(self.btnDevelopment)
        self.layout.addWidget(self.btnTerminalApp)
        self.layout.addStretch()

        # Connect buttons to functions
        self.btnGnome.clicked.connect(lambda: parent.open_window(
            "Gnome Settings", GnomeWin, [self]))
        self.btnExtension.clicked.connect(lambda: parent.open_window(
            "Gnome Extensions", ExtensionsWin, [self]))
        self.btnPamac.clicked.connect(lambda: parent.open_window(
            "Software Manager", PamacWin, [self]))
        self.btnAurHelper.clicked.connect(lambda: parent.open_window(
            "AUR Helper", AurHelperWin, [self]))
        self.btnTheming.clicked.connect(lambda: parent.open_window(
            "Appearance", AppearanceWin, [self]))
        self.btnVariables.clicked.connect(lambda: parent.open_window(
            "Environment Variables", VariableWin, [self]))
        self.btnLure.clicked.connect(lambda: parent.open_window(
            "Linux User Repository", LureWin, [self]))
        self.btnShell.clicked.connect(lambda: parent.open_window(
            "Shell Program & Customizations", ShellWin, [self]))
        self.btnEssentials.clicked.connect(lambda: parent.open_window(
            "Essential Apps", AppsWin, ["Data/Essentials.json", self]))
        self.btnGaming.clicked.connect(lambda: parent.open_window(
            "Gaming Tools", AppsWin, ["Data/Gaming.json", self]))
        self.btnGames.clicked.connect(lambda: parent.open_window(
            "Recommended Games", AppsWin, ["Data/Games.json", self]))
        self.btnDevelopment.clicked.connect(lambda: parent.open_window(
            "Development", AppsWin, ["Data/Development.json", self]))
        self.btnTerminalApp.clicked.connect(lambda: parent.open_window(
            "Terminal Tools", AppsWin, ["Data/Terminal.json", self]))

        # Initialization
        self.check_aur_helper()

    # Check if has AUR helper
    def check_aur_helper(self) -> None:
        installed = has_aur_helper()
        self.btnAurHelper.setStyleSheet(
            "QPushButton { color: " + ("green" if installed else "red") + "; }")
        self.btnAurHelper.setText(
            self.txtAurButton + (". Done!" if installed else ". Urgent!"))
