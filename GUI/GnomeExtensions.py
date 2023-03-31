from PyQt5.QtWidgets import QWidget, QGroupBox, QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from Result import CommandButton
from Utilities import install_if_doesnt_have, ExtensionBox
from json import load


class ExtensionsTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create connector section
        self.gbxConnector = QGroupBox("Browser Connector")
        self.glyConnector = QVBoxLayout(self.gbxConnector)
        self.lblConnector = QLabel(
            "You need to install a browser connector to be able to install extensions from your web browser.", self.gbxConnector)
        self.lblConnector.setWordWrap(True)
        self.btnConnector = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxConnector)
        self.glyConnector.addWidget(self.lblConnector)
        self.glyConnector.addWidget(self.btnConnector)

        # Create Extensions section
        self.gbxExtensions = QGroupBox("Suggested Extensions")
        self.glyExtensions = QGridLayout(self.gbxExtensions)
        self.lblExtensions = QLabel(
            "Here are some suggested extensions to make Gnome better.", self.gbxExtensions)

        self.glyExtensions.addWidget(self.lblExtensions, 0, 0, 1, 3)
        # Connect buttons to functions
        self.btnConnector.clicked.connect(lambda: install_if_doesnt_have(
            "gnome-browser-connector", self.btnConnector))

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxConnector)
        self.layout.addWidget(self.gbxExtensions)
        self.load_extensions()

    def load_extensions(self):
        with open("GUI/Data/Extensions.json", "r") as extensions_json:
            extensions = load(extensions_json)
        for number, extension in enumerate(extensions):
            match number:
                case 1:
                    self.glyExtensions.addWidget(
                        ExtensionBox(*extension), 1, 1)
                case 2:
                    self.glyExtensions.addWidget(
                        ExtensionBox(*extension), 1, 2)
                case _:
                    self.glyExtensions.addWidget(ExtensionBox(*extension))
