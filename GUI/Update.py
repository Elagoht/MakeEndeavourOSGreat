from PyQt5.QtWidgets import QWidget, QGroupBox, QVBoxLayout
from PyQt5.QtGui import QIcon
from Utilities import aur_helper, CommandButton


class UpdateTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create update section
        self.gbxUpdate = QGroupBox("Update", self)
        self.glyUpdate = QVBoxLayout(self.gbxUpdate)
        self.btnUpdate = CommandButton(
            QIcon("GUI/Assets/update.png"), "Update databases", self.gbxUpdate, aur_helper()+" -Sy")
        self.glyUpdate.addWidget(self.btnUpdate)

        # Create upgrade section
        self.gbxUpgrade = QGroupBox("Upgrade", self)
        self.glyUpgrade = QVBoxLayout(self.gbxUpgrade)
        self.btnUpgrade = CommandButton(
            QIcon("GUI/Assets/upgrade.png"), "Upgrade system", self.gbxUpgrade, aur_helper()+" -Su")
        self.glyUpgrade.addWidget(self.btnUpgrade)

        # Add groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxUpdate)
        self.layout.addWidget(self.gbxUpgrade)
