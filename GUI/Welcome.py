from PyQt5.QtWidgets import QWidget, QVBoxLayout
from Utilities import QLabel


class WelcomeWin(QWidget):
    def __init__(self, parent) -> None:
        super(QWidget, self).__init__()
        self.setParent(parent)

        self.lblWelcome = QLabel("""<h1>Welcome to Endeavour OS Tweaker</h1>
            <p>Adapt your computer to your usage patterns by using this application. Click buttons on the left to start tweaking.</p>""")
        self.lblWelcome.setWordWrap(True)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.lblWelcome)
