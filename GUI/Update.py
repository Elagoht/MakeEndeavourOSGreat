from PyQt5.QtWidgets import QWidget, QGroupBox, QVBoxLayout
from PyQt5.QtGui import QIcon
from Utilities import run_command
from Result import CommandButton


class UpdateTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create update section
        self.gbxUpdate = QGroupBox("Update", self)
        self.glyUpdate = QVBoxLayout(self.gbxUpdate)
        self.btnUpdate = CommandButton(
            QIcon("GUI/Assets/update.png"), "Update databases", self.gbxUpdate)
        self.glyUpdate.addWidget(self.btnUpdate)

        # Create upgrade section
        self.gbxUpgrade = QGroupBox("Upgrade", self)
        self.glyUpgrade = QVBoxLayout(self.gbxUpgrade)
        self.btnUpgrade = CommandButton(
            QIcon("GUI/Assets/upgrade.png"), "Upgrade system", self.gbxUpgrade)
        self.glyUpgrade.addWidget(self.btnUpgrade)

        # Add groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxUpdate)
        self.layout.addWidget(self.gbxUpgrade)

        # Connect buttons to functions
        self.btnUpdate.clicked.connect(
            lambda: run_command("sudo pacman -Sy", self.btnUpdate))
        self.btnUpgrade.clicked.connect(
            lambda: run_command("sudo pacman -Su", self.btnUpgrade))
