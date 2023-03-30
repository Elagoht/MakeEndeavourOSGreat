from PyQt5.QtWidgets import QWidget, QGroupBox, QPushButton, QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from Result import ResultWidget
from Utilities import install_if_doesnt_have, ExtensionBox


ExtensionList = [
    ["Appindicator Support",
        "https://extensions.gnome.org/extension/615/appindicator-support/",
        "GUI/Assets/Extensions/appindicator.png"],
    ["Dash to Dock",
        "https://extensions.gnome.org/extension/307/dash-to-dock/",
        "GUI/Assets/Extensions/dashtodock.png"],
    ["NoAnnoyance v2",
        "https://extensions.gnome.org/extension/2182/noannoyance/",
        "GUI/Assets/Extensions/noannoyance.png"],
    ["Scroll Panel",
        "https://extensions.gnome.org/extension/4257/scroll-panel/",
        "GUI/Assets/Extensions/scrollpanel.png"],
    ["Force Quit",
        "https://extensions.gnome.org/extension/770/force-quit/",
        "GUI/Assets/Extensions/forcequit.png"],
    ["Caffeine",
        "https://extensions.gnome.org/extension/517/caffeine/",
        "GUI/Assets/Extensions/caffeine.png"],
    ["Add to Desktop",
        "https://extensions.gnome.org/extension/3240/add-to-desktop/",
        "GUI/Assets/Extensions/addtodesktop.png"],
    ["Transparent Window",
        "https://extensions.gnome.org/extension/1454/transparent-window/",
        "GUI/Assets/Extensions/transparent.png"],
    ["OpenWeather",
        "https://extensions.gnome.org/extension/750/openweather/",
        "GUI/Assets/Extensions/openweather.png"],
    ["Statusarea Horizontal Spacing",
        "https://extensions.gnome.org/extension/355/status-area-horizontal-spacing/",
        "GUI/Assets/Extensions/statusareaspacing.png"],
    ["Blur My Shell",
        "https://extensions.gnome.org/extension/3193/blur-my-shell/",
        "GUI/Assets/Extensions/blurmyshell.png"],
    ["Compiz Alike Magic Lamp Effect",
        "https://extensions.gnome.org/extension/3740/compiz-alike-magic-lamp-effect/",
        "GUI/Assets/Extensions/compiz.png"],
    ["Color Picker",
        "https://extensions.gnome.org/extension/3396/color-picker/",
        "GUI/Assets/Extensions/colorpicker.png"],
]


class ExtensionsTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create connector section
        self.gbxConnector = QGroupBox("Browser Connector")
        self.glyConnector = QVBoxLayout(self.gbxConnector)
        self.lblConnector = QLabel(
            "You need to install a browser connector to be able to install extensions from your web browser.", self.gbxConnector)
        self.lblConnector.setWordWrap(True)
        self.btnConnector = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxConnector)
        self.resConnector = ResultWidget()
        self.glyConnector.addWidget(self.lblConnector)
        self.glyConnector.addWidget(self.btnConnector)
        self.glyConnector.addWidget(self.resConnector)

        # Create Extensions section
        self.gbxExtensions = QGroupBox("Suggested Extensions")
        self.glyExtensions = QGridLayout(self.gbxExtensions)
        self.lblExtensions = QLabel(
            "Here are some suggested extensions to make Gnome better.", self.gbxExtensions)
        self.glyExtensions.addWidget(self.lblExtensions, 0, 0, 1, 3)
        self.glyExtensions.addWidget(ExtensionBox(*ExtensionList[0]))
        self.glyExtensions.addWidget(ExtensionBox(*ExtensionList[1]), 1, 1)
        self.glyExtensions.addWidget(ExtensionBox(*ExtensionList[2]), 1, 2)
        for extension in ExtensionList[3:]:
            self.glyExtensions.addWidget(ExtensionBox(*extension))

        # Connect buttons to functions
        self.btnConnector.clicked.connect(lambda: install_if_doesnt_have(
            "gnome-browser-connector", self.resConnector))

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxConnector)
        self.layout.addWidget(self.gbxExtensions)
