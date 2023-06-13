from PyQt5.QtWidgets import QWidget, QVBoxLayout
from Utilities import QLabel


class WelcomeWin(QWidget):
    def __init__(self, parent) -> None:
        super().__init__()
        self.setParent(parent)

        with open("HTML/Welcome.html") as file:
            content = file.read()

        self.lblWelcome = QLabel(content)
        self.lblWelcome.setWordWrap(True)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.lblWelcome)
