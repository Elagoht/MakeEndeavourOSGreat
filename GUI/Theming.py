from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from json import load
from Utilities import ThemeBox, GridBox, ButtonBox, CommandButton


class AppearanceWin(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)

        # Create Kvantum config section
        self.gbxKvantum = \
            ButtonBox("Kvantum QT Theme Setter", "GUI/Assets/Tweaks/kvantum.png",
                      """<p>Qt applications does not follow GTK themes by default. You can use kvantum to manage Qt applications' (like this one) themes. There is an alternative to kvantum, named qt5ct. But updating that is a bit painful.</p>
                         <p>You can change Qt themes thanks to Kvantum Manager. You can set <font color="orange">KvLibadwaita(Dark)</font> theme to uniform themes with Adw-gtk3 theme.</p>
                         <p>Note that: <u>Enable/disable actions require restart.</u></p>""", (
                          CommandButton(QIcon("GUI/Assets/enabled.png"), "Enable Kvantum",
                                        """sudo sed -i "s/^\#QT_STYLE_OVERRIDE=kvantum/QT_STYLE_OVERRIDE=kvantum/" /etc/environment
                                if [ ! "$(grep '^QT_STYLE_OVERRIDE=kvantum' /etc/environment)" ]
                                    then sudo echo "QT_STYLE_OVERRIDE=kvantum" >> /etc/environment
                                fi""", self),
                          CommandButton(QIcon("GUI/Assets/disabled.png"), "Disable Kvantum",
                                        """if [ "$(grep '^QT_STYLE_OVERRIDE=kvantum' /etc/environment)" ]
                                    then sudo sed -i "s/^QT_STYLE_OVERRIDE=kvantum/#QT_STYLE_OVERRIDE=kvantum/" /etc/environment
                                fi""", self),
                          CommandButton(
                              QIcon("GUI/Assets/configure.png"),
                              "Open Kvantum Manager", "kvantummanager",
                              self, [], True, True),))

        # Create GTK themes section
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
        self.load_themes("GUI/Data/Fonts.json", 3, self.gbxFont)

        # Insert groupboxes to layout

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxKvantum)
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
