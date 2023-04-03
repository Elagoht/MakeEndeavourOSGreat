from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from Utilities import ButtonBox, GridBox, CommandButton


class GnomeTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create Wayland section
        self.gbxWayland = ButtonBox(
            "Wayland Settings", "GUI/Assets/Tweaks/wayland.png",
            "<p>Wayland is a new technology to replace Xorg display server. Its may be lighter and faster. Waydroid only works on Wayland but because of it is a new technology, some features are not compatible yet. I.e. global keyboard shourtcuts does not supported right now. Discord cannot share screen on.</p>\
            <p>Wayland has its own <font color='green'>advantages</font> and <font color='red'>disadvantages</font>. So you may want to change this setting in the future depending on your needs. But for now using Xorg and ditching Wayland is more compatible.</p>\
            <p><u>Changes require restart.</u></p>", (
                CommandButton(QIcon("GUI/Assets/configure.png"),
                              "Use Wayland", self),
                CommandButton(QIcon("GUI/Assets/configure.png"),
                              "Use XOrg", self)
            ), (
                "sudo sed -i \"s/^WaylandEnable=false/#WaylandEnable=false/\" /etc/gdm/custom.conf",
                "sudo sed -i \"s/^#WaylandEnable=false/WaylandEnable=false/\" /etc/gdm/custom.conf"
            )
        )

        # Create context menu section
        self.gbxContext = ButtonBox(
            "Context Menu", "GUI/Assets/Tweaks/contextmenu.png", "Enable context (right click) menu icons.", (
                CommandButton(QIcon("GUI/Assets/enabled.png"),
                              "Enable Icons", self),
                CommandButton(QIcon("GUI/Assets/disabled.png"),
                              "Disable Icons", self)
            ), (
                "gsettings set org.gnome.settings-daemon.plugins.xsettings overrides \"{\\\"Gtk/ButtonImages\\\": <1>, \\\"Gtk/MenuImages\\\": <1>}\"",
                "gsettings set org.gnome.settings-daemon.plugins.xsettings overrides \"{}\""
            ))

        # Create Gnome Terminal/Console section
        self.gbxTerm = GridBox("Gnome Terminal / Console")
        # Chose Gnome Terminal over Console
        self.appTerminal = ButtonBox("Gnome Terminal", "GUI/Assets/Tweaks/gnometerminal.png",
                                     "Gnome terminal is more compatible than console with Gnome desktop environment (open with terminal etc.). But may not be able to adapt dark/light theme. <u>Transparency support is serving separately.</u> Chose one.", (
                                         CommandButton(
                                             QIcon("GUI/Assets/configure.png"), "Use Terminal", self),
                                         CommandButton(
                                             QIcon("GUI/Assets/configure.png"), "Use Transparent Terminal", self),
                                     ), (
                                         """if [ ! "$(pacman -Qqs gnome-terminal | grep ^gnome-terminal$)" = "gnome-terminal" ]
                                                then sudo pacman -S gnome-terminal
                                            fi &&
                                            if [ -f /usr/bin/kgx ]
                                                then sudo pacman -R gnome-console
                                            fi""",
                                         """if [ ! "$(pacman -Qqs gnome-terminal-transparency | grep ^gnome-terminal-transparency$)" = "gnome-terminal-transparency" ]
                                                then sudo pacman -S gnome-terminal-transparency
                                            fi &&
                                            if [ -f /usr/bin/kgx ]
                                                then sudo pacman -R gnome-console
                                            fi"""
                                     ))
        # Chose Gnome Console over Terminal
        self.appConsole = ButtonBox("Gnome Console", "GUI/Assets/Tweaks/gnomeconsole.png",
                                    "Gnome Console is more compatible with dark/light theme but is not compatible with default terminal application configuration.", (
                                        CommandButton(
                                            QIcon("GUI/Assets/configure.png"), "Use Gnome Console", self),
                                    ), (
                                        """[ ! -f /usr/bin/kgx ] && sudo pacman -S gnome-console &&
                                            if [ "$(pacman -Qqs gnome-terminal)" = "gnome-terminal-transparency" ]
                                                then sudo pacman -R gnome-terminal-transparency
                                            elif [ "$(pacman -Qqs gnome-terminal)" = "gnome-terminal" ]
                                                then sudo pacman -R gnome-terminal
                                            fi""",
                                    ))
        self.gbxTerm.addWidget(self.appTerminal)
        self.gbxTerm.addWidget(self.appConsole, 0, 1)

        # Insert groupboxes into layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxWayland)
        self.layout.addWidget(self.gbxContext)
        self.layout.addWidget(self.gbxTerm)
