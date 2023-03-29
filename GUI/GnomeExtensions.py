from PyQt5.QtWidgets import QWidget, QGroupBox, QPushButton, QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from RunCommand import run_command
from Result import ResultWidget
from os import popen
from Utilities import aur_helper, has_aur_helper


ExtensionList = {
    "Appindicator Support": "https://extensions.gnome.org/extension/615/appindicator-support/",
    "Dash to Dock": "https://extensions.gnome.org/extension/307/dash-to-dock/",
    "NoAnnoyance v2": "https://extensions.gnome.org/extension/2182/noannoyance/",
    "Scroll Panel": "https://extensions.gnome.org/extension/4257/scroll-panel/",
    "Force Quit": "https://extensions.gnome.org/extension/770/force-quit/",
    "Caffeine": "https://extensions.gnome.org/extension/517/caffeine/",
    "Add to Desktop": "https://extensions.gnome.org/extension/3240/add-to-desktop/",
    "Transparent Window": "https://extensions.gnome.org/extension/1454/transparent-window/",
    "OpenWeather": "https://extensions.gnome.org/extension/750/openweather/",
    "Statusarea Horizontal Spacing": "https://extensions.gnome.org/extension/355/status-area-horizontal-spacing/",
    "Blur My Shell": "https://extensions.gnome.org/extension/3193/blur-my-shell/",
    "Compiz Alike Magic Lamp Effect": "https://extensions.gnome.org/extension/3740/compiz-alike-magic-lamp-effect/",
    "Color Picker": "https://extensions.gnome.org/extension/3396/color-picker/"
}

extensions = ""
for name, link in ExtensionList.items():
    extensions += "<li><a href =\""+link+"\">"+name+"</a></li>"


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
            """Here are some suggested extensions:
<ul>""" + extensions + """
</ul>""",
            self.gbxExtensions)
        self.lblExtensions.setWordWrap(True)
        self.lblExtensions.setOpenExternalLinks(True)
        self.lblExtensions.setTextFormat(Qt.RichText)
        self.lblExtensions.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.glyExtensions.addWidget(self.lblExtensions)

        # Connect buttons to functions
        self.btnConnector.clicked.connect(lambda: run_command(
            f"""if [ ! "$(pacman -Qqs gnome-browser-connector)" = "gnome-browser-connector" ]
    then {aur_helper()} -S gnome-browser-connector
fi""" if has_aur_helper() else "false", self.resConnector))

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxConnector)
        self.layout.addWidget(self.gbxExtensions)
