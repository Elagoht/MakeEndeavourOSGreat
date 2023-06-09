from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from Utilities import ExtensionBox, AppBox, GridBox, get_installed_apps
from json import load


class ExtensionsWin(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.setParent(parent)

        # Create connector section
        self.installed_apps = get_installed_apps()
        self.gbxConnector = AppBox("Browser Connector", "gnome-browser-connector", "Assets/Apps/gnomeextensions.png",
                                   "To install extensions from your web browser, you will need to install a browser connector.",
                                   self, self.parent().parent().barBottom)

        # Create Extensions section
        self.gbxExtensions = GridBox("Suggested Extensions")
        self.lblExtensions = QLabel(
            "Here are some suggested extensions to enhance your GNOME experience:", self.gbxExtensions)
        self.gbxExtensions.addWidget(self.lblExtensions, 0, 0, 1, 3)

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxConnector)
        self.layout.addWidget(self.gbxExtensions)
        self.load_extensions()
        self.layout.addStretch()

    def load_extensions(self):
        with open("Data/Extensions.json", "r") as extensions_json:
            extensions = load(extensions_json)
        for number, extension in enumerate(extensions):
            match number:
                case 1:
                    self.gbxExtensions.addWidget(
                        ExtensionBox(*extension), 1, 1)
                case 2:
                    self.gbxExtensions.addWidget(
                        ExtensionBox(*extension), 1, 2)
                case _:
                    self.gbxExtensions.glyField.addWidget(
                        ExtensionBox(*extension))
