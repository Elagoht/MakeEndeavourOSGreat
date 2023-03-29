from PyQt5.QtWidgets import QTabWidget
from Gnome import GnomeTab
from Update import UpdateTab
from Pamac import PamacTab


class Central(QTabWidget):
    def __init__(self):
        super(Central, self).__init__()

        # Create tab widgets
        self.GnomeTab = GnomeTab()
        self.UpdateTab = UpdateTab()
        self.PamacTab = PamacTab()

        # Insert tab widgets
        self.insertTab(0, self.UpdateTab, "Update System")
        self.insertTab(1, self.GnomeTab, "Gnome Options")
        self.insertTab(2, self.PamacTab, "Sofware Manager")
