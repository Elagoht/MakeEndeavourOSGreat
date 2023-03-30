from PyQt5.QtWidgets import QWidget, QGroupBox, QPushButton, QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from Result import ResultWidget
from Utilities import run_command, install_if_doesnt_have
from os import popen


class ThemingTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create fonts section
        self.gbxFont = QGroupBox("Nerd Font Configuration")
        self.glyFont = QGridLayout(self.gbxFont)
        self.lblFont = QLabel(
            "Nerd fonts are font collections formed by combining alphanumerical and symbolic characters. Includes lots of font-icon and have wide use area. To be able to see font-icons instead of empty rectangle, install and use one of the following.", self.gbxFont)
        self.lblFont.setWordWrap(True)
        self.lblUbuntu = QLabel("Ubuntu Mono Nerd", self.gbxFont)
        self.btnUbuntu = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxFont)
        self.btnUbuntuSet = QPushButton(
            QIcon("GUI/Assets/enabled.png"), "Set Active", self.gbxFont)
        self.resUbuntu = ResultWidget()
        self.resUbuntuSet = ResultWidget()
        self.lblSource = QLabel("Source Code Pro Nerd", self.gbxFont)
        self.btnSource = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxFont)
        self.btnSourceSet = QPushButton(
            QIcon("GUI/Assets/enabled.png"), "Set Active", self.gbxFont)
        self.resSource = ResultWidget()
        self.resSourceSet = ResultWidget()
        self.lblRoboto = QLabel("Roboto Mono Nerd", self.gbxFont)
        self.btnRoboto = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxFont)
        self.btnRobotoSet = QPushButton(
            QIcon("GUI/Assets/enabled.png"), "Set Active", self.gbxFont)
        self.resRoboto = ResultWidget()
        self.resRobotoSet = ResultWidget()
        self.lblJetbrains = QLabel("Jetbrains Mono Nerd", self.gbxFont)
        self.btnJetbrains = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxFont)
        self.btnJetbrainsSet = QPushButton(
            QIcon("GUI/Assets/enabled.png"), "Set Active", self.gbxFont)
        self.resJetbrains = ResultWidget()
        self.resJetbrainsSet = ResultWidget()
        self.lblFiraCode = QLabel("FiraCode Nerd", self.gbxFont)
        self.btnFiraCode = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxFont)
        self.btnFiraCodeSet = QPushButton(
            QIcon("GUI/Assets/enabled.png"), "Set Active", self.gbxFont)
        self.resFiraCode = ResultWidget()
        self.resFiraCodeSet = ResultWidget()
        self.lblDroid = QLabel("Droid Mono Nerd", self.gbxFont)
        self.btnDroid = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxFont)
        self.btnDroidSet = QPushButton(
            QIcon("GUI/Assets/enabled.png"), "Set Active", self.gbxFont)
        self.resDroid = ResultWidget()
        self.resDroidSet = ResultWidget()
        self.lblDejavu = QLabel("Dejavu Mono Nerd", self.gbxFont)
        self.btnDejavu = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxFont)
        self.btnDejavuSet = QPushButton(
            QIcon("GUI/Assets/enabled.png"), "Set Active", self.gbxFont)
        self.resDejavu = ResultWidget()
        self.resDejavuSet = ResultWidget()
        self.lblHack = QLabel("Hack Nerd", self.gbxFont)
        self.btnHack = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install", self.gbxFont)
        self.btnHackSet = QPushButton(
            QIcon("GUI/Assets/enabled.png"), "Set Active", self.gbxFont)
        self.resHack = ResultWidget()
        self.resHackSet = ResultWidget()
        self.glyFont.addWidget(self.lblFont, 0, 0, 1, 3)
        self.glyFont.addWidget(self.lblUbuntu, 1, 0)
        self.glyFont.addWidget(self.btnUbuntu, 1, 1)
        self.glyFont.addWidget(self.btnUbuntuSet, 1, 2)
        self.glyFont.addWidget(self.resUbuntu, 2, 1)
        self.glyFont.addWidget(self.resUbuntuSet, 2, 2)
        self.glyFont.addWidget(self.lblSource, 3, 0)
        self.glyFont.addWidget(self.btnSource, 3, 1)
        self.glyFont.addWidget(self.btnSourceSet, 3, 2)
        self.glyFont.addWidget(self.resSource, 4, 1)
        self.glyFont.addWidget(self.resSourceSet, 4, 2)
        self.glyFont.addWidget(self.lblRoboto, 5, 0)
        self.glyFont.addWidget(self.btnRoboto, 5, 1)
        self.glyFont.addWidget(self.btnRobotoSet, 5, 2)
        self.glyFont.addWidget(self.resRoboto, 6, 1)
        self.glyFont.addWidget(self.resRobotoSet, 6, 2)
        self.glyFont.addWidget(self.lblJetbrains, 7, 0)
        self.glyFont.addWidget(self.btnJetbrains, 7, 1)
        self.glyFont.addWidget(self.btnJetbrainsSet, 7, 2)
        self.glyFont.addWidget(self.resJetbrains, 8, 1)
        self.glyFont.addWidget(self.resJetbrainsSet, 8, 2)
        self.glyFont.addWidget(self.lblFiraCode, 9, 0)
        self.glyFont.addWidget(self.btnFiraCode, 9, 1)
        self.glyFont.addWidget(self.btnFiraCodeSet, 9, 2)
        self.glyFont.addWidget(self.resFiraCode, 10, 1)
        self.glyFont.addWidget(self.resFiraCodeSet, 10, 2)
        self.glyFont.addWidget(self.lblDroid, 11, 0)
        self.glyFont.addWidget(self.btnDroid, 11, 1)
        self.glyFont.addWidget(self.btnDroidSet, 11, 2)
        self.glyFont.addWidget(self.resDroid, 12, 1)
        self.glyFont.addWidget(self.resDroidSet, 12, 2)
        self.glyFont.addWidget(self.lblDejavu, 13, 0)
        self.glyFont.addWidget(self.btnDejavu, 13, 1)
        self.glyFont.addWidget(self.btnDejavuSet, 13, 2)
        self.glyFont.addWidget(self.resDejavu, 14, 1)
        self.glyFont.addWidget(self.resDejavuSet, 14, 2)
        self.glyFont.addWidget(self.lblHack, 15, 0)
        self.glyFont.addWidget(self.btnHack, 15, 1)
        self.glyFont.addWidget(self.btnHackSet, 15, 2)
        self.glyFont.addWidget(self.resHack, 16, 1)
        self.glyFont.addWidget(self.resHackSet, 16, 2)

        # Connect buttons to functions
        self.btnUbuntu.clicked.connect(lambda: install_if_doesnt_have(
            "ttf-ubuntu-mono-nerd", self.resUbuntu))
        self.btnUbuntuSet.clicked.connect(lambda: self.change_font_family(
            "UbuntuMono Nerd Font Mono", self.resUbuntuSet))
        self.btnSource.clicked.connect(lambda: install_if_doesnt_have(
            "ttf-sourcecodepro-nerd", self.resSource))
        self.btnSourceSet.clicked.connect(lambda: self.change_font_family(
            "Source Code Pro", self.resSourceSet))
        self.btnRoboto.clicked.connect(lambda: install_if_doesnt_have(
            "ttf-roboto-mono-nerd", self.resRoboto))
        self.btnRobotoSet.clicked.connect(lambda: self.change_font_family(
            "RobotoMono Nerd Font Mono", self.resRobotoSet))
        self.btnJetbrains.clicked.connect(lambda: install_if_doesnt_have(
            "ttf-jetbrains-mono-nerd", self.resJetbrains))
        self.btnJetbrainsSet.clicked.connect(lambda: self.change_font_family(
            "JetBrainsMono Nerd Font Mono", self.resJetbrainsSet))
        self.btnFiraCode.clicked.connect(lambda: install_if_doesnt_have(
            "ttf-firacode-nerd", self.resFiraCode))
        self.btnFiraCodeSet.clicked.connect(lambda: self.change_font_family(
            "FiraCode Nerd Font Mono", self.resFiraCodeSet))
        self.btnDroid.clicked.connect(lambda: install_if_doesnt_have(
            "otf-droid-nerd", self.resDroid))
        self.btnDroidSet.clicked.connect(lambda: self.change_font_family(
            "DroidSansMono Nerd Font Mono", self.resDroidSet))
        self.btnDejavu.clicked.connect(lambda: install_if_doesnt_have(
            "ttf-dejavu-nerd", self.resDejavu))
        self.btnDejavuSet.clicked.connect(lambda: self.change_font_family(
            "DejaVuSansMono Nerd Font Mono", self.resDejavuSet))
        self.btnHack.clicked.connect(lambda: install_if_doesnt_have(
            "ttf-hack-nerd", self.resHack))
        self.btnHackSet.clicked.connect(lambda: self.change_font_family(
            "Hack Nerd Font Mono", self.resHackSet))

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxFont)

    def change_font_family(self, font_family: str, result_widget: ResultWidget):
        font_size = popen(
            "gsettings get org.gnome.desktop.interface monospace-font-name")\
            .readline().strip().split()[-1].replace("'", "")
        print(
            f"gsettings set org.gnome.desktop.interface monospace-font-name \"{font_family} {font_size}\"")
        run_command(
            f"gsettings set org.gnome.desktop.interface monospace-font-name \"{font_family} {font_size}\"",
            result_widget)
