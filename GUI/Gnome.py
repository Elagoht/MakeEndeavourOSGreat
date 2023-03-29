from PyQt5.QtWidgets import QLineEdit, QMainWindow, QSpinBox, QWidget, QGroupBox, QPushButton, QLabel, QVBoxLayout, QStatusBar
from PyQt5.QtGui import QIcon
from RunCommand import run_command
from Result import ResultWidget


class GnomeTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

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
            "Gnome terminal is more compatible than console with Gnome desktop environment (open with terminal etc.). But may not be able to adapt dark/light theme.")
        self.lblConsole.setWordWrap(True)
        self.btnConsole = QPushButton(
            QIcon("GUI/Assets/install.png"), "Install Gnome Terminal", self.gbxConsole)
        self.resConsole = ResultWidget()
        self.glyConsole.addWidget(self.lblConsole)
        self.glyConsole.addWidget(self.btnConsole)
        self.glyConsole.addWidget(self.resConsole)

        self.glyTerm.addWidget(self.gbxTerminal)
        self.glyTerm.addWidget(self.gbxConsole)

        # Connect buttons to functions
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

        # Insert groupboxes into layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxTerm)
