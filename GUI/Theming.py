from PyQt5.QtWidgets import QWidget, QGroupBox, QPushButton, QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from Result import CommandButton
from Utilities import run_command, install_if_doesnt_have, uninstall_if_have
from os import popen, system, WEXITSTATUS


class ThemingTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create fonts section
        self.gbxFont = QGroupBox("Nerd Font Configuration")
        self.glyFont = QGridLayout(self.gbxFont)
        self.lblFont = QLabel("Nerd fonts are font collections formed by combining alphanumerical and symbolic characters. Includes lots of font-icon and have wide use area. To be able to see font-icons instead of empty rectangle, install and use one of the following.", self.gbxFont)
        self.lblFont.setWordWrap(True)
        self.fntUbuntu = FontBox("UbuntuMono Nerd Font Mono ",
                                 "ttf-ubuntu-mono-nerd")
        self.fntSource = FontBox("Source Code Pro",
                                 "ttf-sourcecodepro-nerd")
        self.fntRoboto = FontBox("RobotoMono Nerd Font Mono",
                                 "ttf-roboto-mono-nerd")
        self.fntJetBrains = FontBox("JetBrainsMono Nerd Font Mono",
                                    "ttf-jetbrains-mono-nerd")
        self.fntFiraCode = FontBox("FiraCode Nerd Font Mono",
                                   "ttf-firacode-nerd")
        self.fntDroid = FontBox("DroidSansMono Nerd Font Mono",
                                "otf-droid-nerd")
        self.fntDejavu = FontBox("DejaVuSansMono Nerd Font Mono",
                                 "ttf-dejavu-nerd")
        self.fntHack = FontBox("Hack Nerd Font Mono",
                               "ttf-hack-nerd")
        self.glyFont.addWidget(self.lblFont, 0, 0, 1, 2)
        self.glyFont.addWidget(self.fntUbuntu, 1, 0)
        self.glyFont.addWidget(self.fntSource, 1, 1)
        self.glyFont.addWidget(self.fntRoboto)
        self.glyFont.addWidget(self.fntJetBrains)
        self.glyFont.addWidget(self.fntFiraCode)
        self.glyFont.addWidget(self.fntDroid)
        self.glyFont.addWidget(self.fntDejavu)
        self.glyFont.addWidget(self.fntHack)

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxFont)


class FontBox(QGroupBox):
    def __init__(self, name: str, package: str):
        super(QGroupBox, self).__init__()
        self.setTitle(name)
        self.glyFont = QGridLayout(self)
        self.btnFontInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install", self)
        self.btnFontUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall", self)
        self.btnFontSet = CommandButton(
            QIcon("GUI/Assets/enabled.png"), "Select", self)
        self.glyFont.addWidget(self.btnFontInstall)
        self.glyFont.addWidget(self.btnFontUninstall, 0, 1)
        self.glyFont.addWidget(self.btnFontSet, 0, 2)

        # Connect buttons to functions
        self.btnFontInstall.clicked.connect(
            lambda: install_if_doesnt_have(package, self.btnFontInstall))
        self.btnFontUninstall.clicked.connect(
            lambda: uninstall_if_have(package, self.btnFontUninstall))
        self.btnFontSet.clicked.connect(
            lambda: self.change_font_family(name, package, self.btnFontSet))

    def change_font_family(self, font_family: str, package: str, result_widget: CommandButton) -> None:
        if WEXITSTATUS(system(f"[ ! \"$(pacman -Qqs {package} | grep \"^{package}$\")\" = \"{package}\" ]")) == 0:
            result_widget.setStatus(-1)
            return
        font_size = popen(
            "gsettings get org.gnome.desktop.interface monospace-font-name")\
            .readline().strip().split()[-1].replace("'", "")
        print(
            f"gsettings set org.gnome.desktop.interface monospace-font-name \"{font_family} {font_size}\"")
        run_command(
            f"gsettings set org.gnome.desktop.interface monospace-font-name \"{font_family} {font_size}\"",
            result_widget)
