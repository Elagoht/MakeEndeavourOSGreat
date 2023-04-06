from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from Utilities import GridBox
from json import load
from Utilities import FontBox, ThemeBox


class AppearanceWin(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create themes section
        self.gbxTheme = GridBox("GTK Themes")
        self.lblTheme = QLabel(
            """<p>This is the primary theme for your interface and apps that use GTK framwork.</p>
            <p>You MUST use "Awd-gtk3" to unify the themes. There are other themes. GTK 4 apps does not properly adapt to other themes yet.</p>""", self.gbxTheme)
        self.lblTheme.setWordWrap(True)
        self.gbxTheme.addWidget(self.lblTheme, 0, 0, 1, 3)
        self.load_themes("GUI/Data/Themes.json", 0, self.gbxTheme)

        # Create icons section
        self.gbxIcons = GridBox("Icons Themes")
        self.lblIcons = QLabel(
            "Icons themes determines how your apps, mimetypes, folders, actions, categories, emblems, panel status will look.", self.gbxIcons)
        self.lblIcons.setWordWrap(True)
        self.gbxIcons.addWidget(self.lblIcons, 0, 0, 1, 3)
        self.load_themes("GUI/Data/Icons.json", 1, self.gbxIcons)

        # Create cursor section
        self.gbxCursor = GridBox("Cursor Themes")
        self.lblCursor = QLabel(
            "Cursor themes determines how your mouse pointer will look.", self.gbxCursor)
        self.lblCursor.setWordWrap(True)
        self.gbxCursor.addWidget(self.lblCursor, 0, 0, 1, 3)
        self.load_themes("GUI/Data/Cursors.json", 2, self.gbxCursor)

        # Create fonts section
        self.gbxFont = GridBox("Nerd Fonts")
        self.lblFont = QLabel(
            "Nerd fonts are font collections formed by combining alphanumerical and symbolic characters. Includes lots of font-icon and have wide use area. To be able to see font-icons instead of empty rectangle, install and use one of the following.", self.gbxFont)
        self.lblFont.setWordWrap(True)
        self.gbxFont.addWidget(self.lblFont, 0, 0, 1, 3)
        self.load_fonts()

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxTheme)
        self.layout.addWidget(self.gbxIcons)
        self.layout.addWidget(self.gbxCursor)
        self.layout.addWidget(self.gbxFont)

    def load_themes(self, file: str, type: int, widget: GridBox):
        with open(file, "r") as themes_json:
            themes: list = load(themes_json)
        for number, theme in enumerate(themes):
            match number:
                case 0:
                    widget.addWidget(ThemeBox(*theme.values(), type), 1, 0)
                case 1:
                    widget.addWidget(ThemeBox(*theme.values(), type), 1, 1)
                case 2:
                    widget.addWidget(ThemeBox(*theme.values(), type), 1, 2)
                case _:
                    widget.glyField.addWidget(
                        ThemeBox(*theme.values(), type))

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
