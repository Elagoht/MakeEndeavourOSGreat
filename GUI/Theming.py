from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from json import load
from Utilities import ThemeBox, GridBox, ButtonBox, CommandButton


class AppearanceWin(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)

        # Create Kvantum config section
        self.gbxKvantumEnable = \
            ButtonBox("Kvantum QT Theme Setter", "Assets/Tweaks/kvantum.png",
                      """<p>Qt applications does not follow GTK themes by default. You can use kvantum to manage Qt applications' (like this one) themes. There is an alternative to kvantum, named qt5ct. But updating that is a bit painful.</p>
                         <p>You can change Qt themes thanks to Kvantum Manager. You can set <font color="green">KvLibadwaita(Dark)</font> theme to uniform themes with Adw-gtk3 theme.</p>
                         <p>Note that: <u>enabling or disabling actions may require a restart for the changes to take effect.</u></p>""", (
                          CommandButton(QIcon("Assets/enabled.png"), "Enable Kvantum",
                                        """pkexec sed -i "s/^\#QT_STYLE_OVERRIDE=kvantum/QT_STYLE_OVERRIDE=kvantum/" /etc/environment;
                                if [ ! "$(grep '^QT_STYLE_OVERRIDE=kvantum' /etc/environment)" ]
                                    then pkexec sh -c "cat >> /etc/environment << EOF

QT_STYLE_OVERRIDE=kvantum
EOF"
                                fi""", self),
                          CommandButton(QIcon("Assets/disabled.png"), "Disable Kvantum",
                                        """if [ "$(grep '^QT_STYLE_OVERRIDE=kvantum' /etc/environment)" ]
                                    then pkexec sed -i "s/^QT_STYLE_OVERRIDE=kvantum/#QT_STYLE_OVERRIDE=kvantum/" /etc/environment
                                fi""", self),
                          CommandButton(
                              QIcon("Assets/configure.png"),
                              "Open Kvantum Manager", "kvantummanager",
                              self, [], True, True),))

        # Create GTK themes section
        self.gbxTheme = GridBox("GTK Themes")
        self.lblTheme = QLabel(
            """This is the primary theme for your interface and applications that utilize the GTK framework. It is essential to use "Adw-gtk3" to ensure theme consistency. While there are other themes available, it's important to note that GTK 4 applications may not fully adapt to these themes yet.""", self.gbxTheme)
        self.lblTheme.setWordWrap(True)
        self.gbxTheme.addWidget(self.lblTheme, 0, 0, 1, 3)
        self.load_themes("Data/Themes.json", 0, self.gbxTheme)

        # Create Kvantum themes section
        self.gbxKvantum = GridBox("Kvantum Themes")
        self.lblKvantum = QLabel(
            "This is the primary Qt theme for your interface. <u>If you changed theme settings in Kvantum Manager, you may need to change theme by Kvantum Manager.</u> Changed themes stores separately.", self.gbxKvantum)
        self.lblKvantum.setWordWrap(True)
        self.gbxKvantum.addWidget(self.lblKvantum, 0, 0, 1, 3)
        self.load_themes("Data/Kvantum.json", 4, self.gbxKvantum)

        # Create icons section
        self.gbxIcons = GridBox("Icons Themes")
        self.lblIcons = QLabel(
            "Icon themes determine the appearance of your applications, mimetypes, folders, actions, categories, emblems, and panel status. They play a significant role in defining the visual representation of various elements in your user interface.", self.gbxIcons)
        self.lblIcons.setWordWrap(True)
        self.gbxIcons.addWidget(self.lblIcons, 0, 0, 1, 3)
        self.load_themes("Data/Icons.json", 1, self.gbxIcons)

        # Create cursor section
        self.gbxCursor = GridBox("Cursor Themes")
        self.lblCursor = QLabel(
            "Cursor themes determine how your mouse pointer will look.", self.gbxCursor)
        self.lblCursor.setWordWrap(True)
        self.gbxCursor.addWidget(self.lblCursor, 0, 0, 1, 3)
        self.load_themes("Data/Cursors.json", 2, self.gbxCursor)

        # Create fonts section
        self.gbxFont = GridBox("Nerd Fonts")
        self.lblFont = QLabel(
            "Nerd fonts are collections of fonts that combine alphanumeric and symbolic characters. They include numerous font icons and have a wide range of applications. To see font icons instead of empty rectangles, you need to install and use one of the following fonts:", self.gbxFont)
        self.lblFont.setWordWrap(True)
        self.gbxFont.addWidget(self.lblFont, 0, 0, 1, 3)
        self.load_themes("Data/Fonts.json", 3, self.gbxFont)

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxKvantumEnable)
        self.layout.addWidget(self.gbxTheme)
        self.layout.addWidget(self.gbxKvantum)
        self.layout.addWidget(self.gbxIcons)
        self.layout.addWidget(self.gbxCursor)
        self.layout.addWidget(self.gbxFont)
        self.layout.addStretch()

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
