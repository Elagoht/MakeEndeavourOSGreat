from PyQt5.QtWidgets import QWidget, QGroupBox, QPushButton, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from RunCommand import run_command
from Result import ResultWidget
from os import popen
from Utilities import aur_helper, has_aur_helper


class GnomeTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create context menu section
        self.gbxContext = QGroupBox("Context Menu", self)
        self.glyContext = QVBoxLayout(self.gbxContext)
        self.lblContext = QLabel("Enable context (right click) menu icons.")
        self.btnContext = QPushButton(
            QIcon("GUI/Assets/configure.png"), "Enable Icons")
        self.resContext = ResultWidget()
        self.glyContext.addWidget(self.lblContext)
        self.glyContext.addWidget(self.btnContext)
        self.glyContext.addWidget(self.resContext)

        # Create terminal and console section
        self.gbxTerm = QGroupBox("Terminal / Console", self)
        self.glyTerm = QVBoxLayout(self.gbxTerm)
        # Chose Gnome Terminal over Console
        self.gbxTerminal = QGroupBox("Gnome Terminal", self)
        self.glyTerminal = QVBoxLayout(self.gbxTerminal)
        self.lblTerminal = QLabel(
            "Gnome terminal is more compatible than console with Gnome desktop environment (open with terminal etc.). But may not be able to adapt dark/light theme.")
        self.lblTerminal.setWordWrap(True)
        self.btnTerminal = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install Gnome Terminal", self.gbxTerminal)
        self.resTerminal = ResultWidget()
        self.glyTerminal.addWidget(self.lblTerminal)
        self.glyTerminal.addWidget(self.btnTerminal)
        self.glyTerminal.addWidget(self.resTerminal)
        # Chose Gnome Console over Terminal
        self.gbxConsole = QGroupBox("Gnome Console", self)
        self.glyConsole = QVBoxLayout(self.gbxConsole)
        self.lblConsole = QLabel(
            "Gnome Console is more compatible with dark/light theme but is not compatible with default terminal application configuration.")
        self.lblConsole.setWordWrap(True)
        self.btnConsole = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install Gnome Console", self.gbxConsole)
        self.resConsole = ResultWidget()
        self.glyConsole.addWidget(self.lblConsole)
        self.glyConsole.addWidget(self.btnConsole)
        self.glyConsole.addWidget(self.resConsole)

        self.glyTerm.addWidget(self.gbxTerminal)
        self.glyTerm.addWidget(self.gbxConsole)

        # Create Gnome terminal transparency section
        self.gbxTransparency = QGroupBox("Gnome Terminal Transparency", self)
        self.glyTransparency = QGridLayout(self.gbxTransparency)
        self.lblTransparency = QLabel(
            "If you use Gnome Terminal, you may want to make your terminal background (semi) transparent. So, you must replace gnome-terminal package with gnome-terminal-transparency.", self.gbxTransparency)
        self.lblTransparency.setWordWrap(True)
        self.lblTransparencyCheck = QLabel(
            "Check your terminal", self.gbxTransparency)
        self.btnTransparencyCheck = QPushButton(
            QIcon("GUI/Assets/check.png"), "Check", self.gbxTransparency)
        self.lblTransparencyResult = QLabel("Start Test")
        self.lblTransparencyResult.setAlignment(Qt.AlignCenter)
        self.lblTransparencyResult.setWordWrap(True)
        self.btnTransparencyInstall = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install Terminal Transparency", self.gbxTransparency)
        self.resTransparencyInstall = ResultWidget()
        self.btnTransparencyUninstall = QPushButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall Terminal Transparency", self.gbxTransparency)
        self.resTransparencyUninstall = ResultWidget()
        self.glyTransparency.addWidget(self.lblTransparency, 0, 0, 1, 2)
        self.glyTransparency.addWidget(self.lblTransparencyCheck, 1, 0, 1, 2)
        self.glyTransparency.addWidget(self.btnTransparencyCheck)
        self.glyTransparency.addWidget(self.lblTransparencyResult)
        self.glyTransparency.addWidget(self.btnTransparencyInstall, 3, 0, 1, 2)
        self.glyTransparency.addWidget(self.resTransparencyInstall, 4, 0, 1, 2)
        self.glyTransparency.addWidget(
            self.btnTransparencyUninstall, 5, 0, 1, 2)
        self.glyTransparency.addWidget(
            self.resTransparencyUninstall, 6, 0, 1, 2)

        # Connect buttons to functions
        self.btnContext.clicked.connect(lambda: run_command(
            "gsettings set org.gnome.settings-daemon.plugins.xsettings overrides \"{\\\"Gtk/ButtonImages\\\": <1>, \\\"Gtk/MenuImages\\\": <1>}\"",
            self.resContext))
        self.btnTerminal.clicked.connect(lambda: run_command(
            """if [ ! -f /bin/gnome-terminal ]
    then sudo pacman -S gnome-terminal
fi &&
if [ -f /usr/bin/kgx ]
    then sudo pacman -R gnome-console
fi""", self.resTerminal))
        self.btnConsole.clicked.connect(lambda: run_command(
            """if [ ! -f /usr/bin/kgx ]
    then sudo pacman -S gnome-console
fi &&
if [ "$(pacman -Qqs gnome-terminal)" = "gnome-terminal-transparency" ]
    then sudo pacman -R gnome-terminal-transparency
elif [ "$(pacman -Qqs gnome-terminal)" = "gnome-terminal" ]
    then sudo pacman -R gnome-terminal
fi""", self.resConsole))
        self.btnTransparencyCheck.clicked.connect(
            lambda: self.lblTransparencyResult.setText(
                self.update_transparency_result(
                    self.check_transparent_terminal())
            ))
        self.btnTransparencyInstall.clicked.connect(lambda: (run_command(
            aur_helper()+" -S gnome-terminal-transparency"
            if has_aur_helper() else "false", self.resTransparencyInstall),
            self.lblTransparencyResult.setText(
                self.update_transparency_result(
                    self.check_transparent_terminal()))))
        self.btnTransparencyUninstall.clicked.connect(lambda: (run_command(
            aur_helper()+" -R gnome-terminal-transparency && sudo pacman -S gnome-terminal"
            if has_aur_helper() else "false", self.resTransparencyUninstall),
            self.lblTransparencyResult.setText(
                self.update_transparency_result(
                    self.check_transparent_terminal()))))

        # Insert groupboxes into layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxContext)
        self.layout.addWidget(self.gbxTerm)
        self.layout.addWidget(self.gbxTransparency)

        # Initialization
        self.btnTransparencyInstall.setDisabled(True)
        self.btnTransparencyUninstall.setDisabled(True)

    def check_transparent_terminal(self) -> int:
        terminal = popen("pacman -Qqs gnome-terminal").readline().strip()
        if terminal == "gnome-terminal":
            return 0
        elif terminal == "gnome-terminal-transparency":
            return 1
        elif popen("pacman -Qqs gnome-console").readline().strip() == "gnome-console":
            return 2
        else:
            return -1

    def update_transparency_result(self, result):
        self.btnTransparencyInstall.setEnabled(result in [0, -1])
        self.btnTransparencyUninstall.setDisabled(result in [0, 2, -1])
        match result:
            case 0:
                return "Available to replace, confirm when asked."
            case 1:
                return "Already installed."
            case 2:
                return "Change terminal first."
            case -1:
                return "Available to install."
