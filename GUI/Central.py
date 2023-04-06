from PyQt5.QtWidgets import QWidget, QScrollArea, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from Utilities import GridBox, AppsWin, CommandButton, aur_helper
from Gnome import GnomeWin
from Pamac import PamacWin
from AurHelper import AurHelperWin
from GnomeExtensions import ExtensionsWin
from Theming import AppearanceWin
from Lure import LureWin
from Shell import ShellWin


class Central(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create welcome section
        self.gbxWelcome = GridBox("Welcome to Endeavour OS Tweaker")
        self.lblWelcome = QLabel(
            "Adapt your computer to your usage patterns by using this application. Click buttons below to start tweaking.")
        self.lblWelcome.setWordWrap(True)
        self.gbxWelcome.addWidget(self.lblWelcome, 0, 0)

        # Create window opener buttons
        self.btnUpdate = CommandButton(
            QIcon("GUI/Assets/upgrade.png"), "Update System",
            aur_helper()+" -Syu", self)
        self.btnGnome = QPushButton("Gnome Settings")
        self.btnExtension = QPushButton("Gnome Extensions")
        self.btnPamac = QPushButton("Software Manager")
        self.btnAurHelper = QPushButton("AUR Helper")
        self.btnLure = QPushButton("LURE")
        self.btnTheming = QPushButton("Appearance")
        self.btnShell = QPushButton("Shell Program")
        self.btnGaming = QPushButton("Gaming Tools")
        self.btnGames = QPushButton("Suggested Games")
        self.btnDevelopment = QPushButton("Development")

        # Insert buttons to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.gbxWelcome, 0, 0, 1, 3)
        self.layout.addWidget(self.btnUpdate, 1, 0)
        self.layout.addWidget(self.btnGnome, 1, 1)
        self.layout.addWidget(self.btnExtension, 1, 2)
        self.layout.addWidget(self.btnPamac)
        self.layout.addWidget(self.btnAurHelper)
        self.layout.addWidget(self.btnLure)
        self.layout.addWidget(self.btnTheming)
        self.layout.addWidget(self.btnShell)
        self.layout.addWidget(self.btnGaming)
        self.layout.addWidget(self.btnGames)
        self.layout.addWidget(self.btnDevelopment)

        # Connect buttons to functions
        self.btnGnome.clicked.connect(lambda: self.open_window(
            "Gnome Settings", GnomeWin))
        self.btnPamac.clicked.connect(lambda: self.open_window(
            "Software Manager", PamacWin))
        self.btnAurHelper.clicked.connect(lambda: self.open_window(
            "AUR Helper", AurHelperWin))
        self.btnExtension.clicked.connect(lambda: self.open_window(
            "Gnome Extensions", ExtensionsWin))
        self.btnTheming.clicked.connect(lambda: self.open_window(
            "Appearance", AppearanceWin, size=QSize(900, 500)))
        self.btnLure.clicked.connect(lambda: self.open_window(
            "Linux User Repository", LureWin))
        self.btnShell.clicked.connect(lambda: self.open_window(
            "Shell Program & Customizations", ShellWin))
        self.btnGaming.clicked.connect(lambda: self.open_window(
            "Gaming Tools", AppsWin, ["GUI/Data/Gaming.json"], QSize(900, 500)))
        self.btnGames.clicked.connect(lambda: self.open_window(
            "Suggested Games", AppsWin, ["GUI/Data/Games.json"], QSize(900, 500)))
        self.btnDevelopment.clicked.connect(lambda: self.open_window(
            "Development", AppsWin, ["GUI/Data/Development.json"], QSize(900, 500)))

    def open_window(self, title: str, window_class: QWidget, params: list = [], size: QSize = QSize(800, 500)):
        self.winWidget = ExternalWindow(title, window_class, params, size)


class ExternalWindow(QWidget):
    def __init__(self, title: str, window_class: QWidget, params: list, size: QSize) -> None:
        super(QWidget, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.scrWidget = QScrollArea(self)
        self.deneme = window_class(*params)
        self.scrWidget.setWidget(self.deneme)
        self.scrWidget.setWidgetResizable(True)
        self.setWindowTitle(title)
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.scrWidget)
        self.setMinimumSize(size)
        self.show()
