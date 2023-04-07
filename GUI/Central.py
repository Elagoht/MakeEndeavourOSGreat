from PyQt5.QtWidgets import QWidget, QScrollArea, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from Utilities import GridBox, AppsWin, CommandButton, aur_helper, has_aur_helper
from Gnome import GnomeWin
from Pamac import PamacWin
from AurHelper import AurHelperWin
from GnomeExtensions import ExtensionsWin
from Theming import AppearanceWin
from Lure import LureWin
from Shell import ShellWin


class Central(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__()
        self.setParent(parent)

        # Declare AUR helper button text to safely edit it later
        self.txtAurButton = "AUR Helper"

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
        self.btnAurHelper = QPushButton(self.txtAurButton)
        self.btnPamac = QPushButton("Software Manager")
        self.btnLure = QPushButton("LURE")
        self.btnGnome = QPushButton("Gnome Settings")
        self.btnExtension = QPushButton("Gnome Extensions")
        self.btnTheming = QPushButton("Appearance")
        self.btnShell = QPushButton("Shell Program")
        self.btnGaming = QPushButton("Gaming Tools")
        self.btnGames = QPushButton("Suggested Games")
        self.btnDevelopment = QPushButton("Development")

        # Insert buttons to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.gbxWelcome, 0, 0, 1, 3)
        self.layout.addWidget(self.btnUpdate, 1, 0)
        self.layout.addWidget(self.btnAurHelper, 1, 1)
        self.layout.addWidget(self.btnPamac, 1, 2)
        self.layout.addWidget(self.btnLure)
        self.layout.addWidget(self.btnGnome)
        self.layout.addWidget(self.btnExtension)
        self.layout.addWidget(self.btnTheming)
        self.layout.addWidget(self.btnShell)
        self.layout.addWidget(self.btnGaming)
        self.layout.addWidget(self.btnGames)
        self.layout.addWidget(self.btnDevelopment)

        # Connect buttons to functions
        self.btnGnome.clicked.connect(lambda: self.open_window(
            "Gnome Settings", GnomeWin))
        self.btnExtension.clicked.connect(lambda: self.open_window(
            "Gnome Extensions", ExtensionsWin))
        self.btnPamac.clicked.connect(lambda: self.open_window(
            "Software Manager", PamacWin))
        self.btnAurHelper.clicked.connect(lambda: self.open_window(
            "AUR Helper", AurHelperWin))
        self.btnTheming.clicked.connect(lambda: self.open_window(
            "Appearance", AppearanceWin))
        self.btnLure.clicked.connect(lambda: self.open_window(
            "Linux User Repository", LureWin))
        self.btnShell.clicked.connect(lambda: self.open_window(
            "Shell Program & Customizations", ShellWin))
        self.btnGaming.clicked.connect(lambda: self.open_window(
            "Gaming Tools", AppsWin, ["GUI/Data/Gaming.json"]))
        self.btnGames.clicked.connect(lambda: self.open_window(
            "Suggested Games", AppsWin, ["GUI/Data/Games.json"]))
        self.btnDevelopment.clicked.connect(lambda: self.open_window(
            "Development", AppsWin, ["GUI/Data/Development.json"]))

        # Check if has AUR helper
        self.check_aur_helper()

    def open_window(self, title: str, window_class: QWidget, params: list = [], size: QSize = QSize(900, 500), caller: QWidget = None) -> None:
        self.winWidget = ExternalWindow(
            title, window_class, params, size, caller=self)

    def check_aur_helper(self) -> None:
        installed = has_aur_helper()
        self.btnAurHelper.setStyleSheet(
            "QPushButton { color: " + ("green" if installed else "red") + "; }")
        self.btnAurHelper.setText(
            self.txtAurButton + ". Done!" if installed else ". Urgent!")


class ExternalWindow(QWidget):
    def __init__(self, title: str, window_class: QWidget, params: list, size: QSize, caller: QWidget) -> None:
        super(QWidget, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.title = title
        self.setWindowTitle(self.title)
        self.scrWidget = QScrollArea(self)
        self.winWidget = window_class(*params)
        self.scrWidget.setWidget(self.winWidget)
        self.scrWidget.setWidgetResizable(True)
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.scrWidget)
        self.setMinimumSize(size)
        self.caller = caller
        self.show()
        self.caller.parent().close()

    def closeEvent(self, event):
        if self.title == "AUR Helper":
            self.caller.check_aur_helper()
        self.caller.parent().center_window()
        self.caller.parent().show()
        event.accept()
