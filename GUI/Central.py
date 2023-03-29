from PyQt5.QtWidgets import QTabWidget, QScrollArea
from Gnome import GnomeTab
from Update import UpdateTab
from Pamac import PamacTab
from AurHelper import AurHelperTab
from GnomeExtensions import ExtensionsTab


class Central(QTabWidget):
    def __init__(self):
        super(QTabWidget, self).__init__()

        # Create tab widgets
        self.GnomeTab = GnomeTab()
        self.UpdateTab = UpdateTab()
        self.PamacTab = PamacTab()
        self.AurHelperTab = AurHelperTab()
        self.ExtensionsTab = ExtensionsTab()

        self.scrollGnome = QScrollArea(self)
        self.scrollGnome.setWidget(self.GnomeTab)
        self.scrollGnome.setWidgetResizable(True)

        self.scrollUpdate = QScrollArea(self)
        self.scrollUpdate.setWidget(self.UpdateTab)
        self.scrollUpdate.setWidgetResizable(True)

        self.scrollPamac = QScrollArea(self)
        self.scrollPamac.setWidget(self.PamacTab)
        self.scrollPamac.setWidgetResizable(True)

        self.scrollAurHelper = QScrollArea(self)
        self.scrollAurHelper.setWidget(self.AurHelperTab)
        self.scrollAurHelper.setWidgetResizable(True)

        self.scrollExtensions = QScrollArea(self)
        self.scrollExtensions.setWidget(self.ExtensionsTab)
        self.scrollExtensions.setWidgetResizable(True)

        # Insert tab widgets
        self.insertTab(0, self.scrollUpdate, "Update System")
        self.insertTab(1, self.scrollPamac, "Sofware Manager")
        self.insertTab(2, self.scrollAurHelper, "AUR Helper")
        self.insertTab(3, self.scrollGnome, "Gnome Options")
        self.insertTab(4, self.scrollExtensions, "Gnome Extensions")
