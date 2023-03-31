from PyQt5.QtWidgets import QWidget, QGroupBox, QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from Result import CommandButton
from Utilities import run_command, install_if_doesnt_have, uninstall_if_have, GridBox
from os import popen, system, WEXITSTATUS
from json import load


class ThemingTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create fonts section
        self.gbxFont = GridBox("Nerd Font Configuration")
        self.lblFont = QLabel("Nerd fonts are font collections formed by combining alphanumerical and symbolic characters. Includes lots of font-icon and have wide use area. To be able to see font-icons instead of empty rectangle, install and use one of the following.", self.gbxFont)
        self.lblFont.setWordWrap(True)
        self.gbxFont.addWidget(self.lblFont, 0, 0, 1, 3)

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxFont)
        self.load_fonts()

    def load_fonts(self):
        with open("GUI/Data/Fonts.json", "r") as fonts_json:
            fonts: dict = load(fonts_json)
        for number, font in enumerate(fonts.items()):
            match number:
                case 0:
                    self.gbxFont.addWidget(FontBox(*font), 1, 0)
                case 1:
                    self.gbxFont.addWidget(FontBox(*font), 1, 1)
                case 2:
                    self.gbxFont.addWidget(FontBox(*font), 1, 2)
                case _:
                    self.gbxFont.glyField.addWidget(FontBox(*font))


class FontBox(QGroupBox):
    def __init__(self, name: str, package: str):
        super(QGroupBox, self).__init__()
        self.glyFont = QGridLayout(self)
        self.lblFontTitle = QLabel(name, self)
        self.lblFontTitle.setWordWrap(True)
        self.btnFontInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install", self)
        self.btnFontUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall", self)
        self.btnFontSet = CommandButton(
            QIcon("GUI/Assets/enabled.png"), "Select", self)
        self.glyFont.addWidget(self.lblFontTitle, 0, 0, 1, 2)
        self.glyFont.addWidget(self.btnFontInstall)
        self.glyFont.addWidget(self.btnFontUninstall)
        self.glyFont.addWidget(self.btnFontSet, 2, 0, 1, 2)
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")

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
