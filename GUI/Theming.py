from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from Utilities import GridBox
from json import load
from Utilities import FontBox, ThemeBox


class ThemingTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create fonts section
        self.gbxTheme = GridBox("GTK Themes")
        self.lblTheme = QLabel(
            "This is the primary theme for your interface and apps that use GTK framwork.", self.gbxTheme)
        self.lblTheme.setWordWrap(True)
        self.gbxTheme.addWidget(self.lblTheme, 0, 0, 1, 3)

        # Create fonts section
        self.gbxFont = GridBox("Nerd Fonts")
        self.lblFont = QLabel("Nerd fonts are font collections formed by combining alphanumerical and symbolic characters. Includes lots of font-icon and have wide use area. To be able to see font-icons instead of empty rectangle, install and use one of the following.", self.gbxFont)
        self.lblFont.setWordWrap(True)
        self.gbxFont.addWidget(self.lblFont, 0, 0, 1, 3)

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxTheme)
        self.layout.addWidget(self.gbxFont)
        self.load_fonts()
        self.load_themes()

    def load_themes(self):
        with open("GUI/Data/Themes.json", "r") as themes_json:
            themes: list = load(themes_json)
        for number, theme in enumerate(themes):
            match number:
                case 0:
                    self.gbxTheme.addWidget(ThemeBox(*theme.values()), 1, 0)
                case 1:
                    self.gbxTheme.addWidget(ThemeBox(*theme.values()), 1, 1)
                case 2:
                    self.gbxTheme.addWidget(ThemeBox(*theme.values()), 1, 2)
                case _:
                    self.gbxTheme.glyField.addWidget(ThemeBox(*theme))

    def load_fonts(self):
        with open("GUI/Data/Fonts.json", "r") as fonts_json:
            fonts: dict = load(fonts_json)
        for number, font in enumerate(fonts.items()):
            match number:
                case 0:
                    self.gbxFont.addWidget(FontBox(*font), 1, 0, 1, 1)
                case 1:
                    self.gbxFont.addWidget(FontBox(*font), 1, 1, 1, 1)
                case 2:
                    self.gbxFont.addWidget(FontBox(*font), 1, 2, 1, 1)
                case _:
                    self.gbxFont.glyField.addWidget(FontBox(*font))
