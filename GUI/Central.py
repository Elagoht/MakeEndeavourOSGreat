from PyQt5.QtWidgets import QTabWidget, QScrollArea
from Gnome import GnomeTab
from Update import UpdateTab
from Pamac import PamacTab
from AurHelper import AurHelperTab
from GnomeExtensions import ExtensionsTab
from Theming import ThemingTab
from Development import DevelopmentTab
from Lure import LureTab


class Central(QTabWidget):
    def __init__(self):
        super(QTabWidget, self).__init__()
        self.setTabPosition(1)

        # Create tab widgets
        self.GnomeTab = GnomeTab()
        self.UpdateTab = UpdateTab()
        self.PamacTab = PamacTab()
        self.AurHelperTab = AurHelperTab()
        self.ExtensionsTab = ExtensionsTab()
        self.ThemingTab = ThemingTab()
        self.DevelopmentTab = DevelopmentTab()
        self.LureTab = LureTab()

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

        self.scrollTheming = QScrollArea(self)
        self.scrollTheming.setWidget(self.ThemingTab)
        self.scrollTheming.setWidgetResizable(True)

        self.scrollDevelopment = QScrollArea(self)
        self.scrollDevelopment.setWidget(self.DevelopmentTab)
        self.scrollDevelopment.setWidgetResizable(True)

        self.scrollLure = QScrollArea(self)
        self.scrollLure.setWidget(self.LureTab)
        self.scrollLure.setWidgetResizable(True)

        # Insert tab widgets
        self.insertTab(0, self.scrollUpdate, "Update System")
        self.insertTab(1, self.scrollPamac, "Sofware Manager")
        self.insertTab(2, self.scrollAurHelper, "AUR Helper")
        self.insertTab(3, self.scrollLure, "LURE")
        self.insertTab(4, self.scrollTheming, "Theming")
        self.insertTab(5, self.scrollGnome, "Gnome Options")
        self.insertTab(6, self.scrollExtensions, "Gnome Extensions")
        self.insertTab(7, self.scrollDevelopment, "Development")
