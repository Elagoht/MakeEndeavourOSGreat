from PyQt5.QtWidgets import QLineEdit, QMainWindow, QSpinBox, QWidget, QGroupBox, QPushButton, QLabel, QGridLayout, QStatusBar, QVBoxLayout
from PyQt5.QtGui import QIcon
from RunCommand import run_command
from Result import ResultWidget


class UpdateTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create update section
        self.gbxUpdate = QGroupBox("Update", self)
        self.glyUpdate = QVBoxLayout(self.gbxUpdate)
        self.btnUpdate = QPushButton(
            QIcon("GUI/Assets/update.png"), "Update databases", self.gbxUpdate)
        self.resUpdate = ResultWidget()
        self.glyUpdate.addWidget(self.btnUpdate)
        self.glyUpdate.addWidget(self.resUpdate)

        # Create upgrade section
        self.gbxUpgrade = QGroupBox("Upgrade", self)
        self.glyUpgrade = QVBoxLayout(self.gbxUpgrade)
        self.btnUpgrade = QPushButton(
            QIcon("GUI/Assets/upgrade.png"), "Upgrade system", self.gbxUpgrade)
        self.resUpgrade = ResultWidget()
        self.glyUpgrade.addWidget(self.btnUpgrade)
        self.glyUpgrade.addWidget(self.resUpgrade)

        # Add groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxUpdate)
        self.layout.addWidget(self.gbxUpgrade)

        # Connect buttons to functions
        self.btnUpdate.clicked.connect(
            lambda: run_command("sudo pacman -Sy", self.resUpdate))
        self.btnUpgrade.clicked.connect(
            lambda: run_command("sudo pacman -Su", self.resUpgrade))

        # Result Widget
