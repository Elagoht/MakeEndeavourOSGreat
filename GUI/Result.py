from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtGui import QIcon


class CommandButton(QPushButton):
    def __init__(self, icon: QIcon, text: str, parent: QWidget):
        super(QPushButton, self).__init__()
        self.text = text
        self.setText(self.text)
        self.setIcon(icon)

    def setStatus(self, statusCode):
        status_icon = ""
        match statusCode:
            case 0:
                self.setStyleSheet("color: green")
                status_icon = "🗸"
            case -1:
                self.setStyleSheet("color: gray")
                status_icon = "☠"
            case _:
                self.setStyleSheet("color: red")
                status_icon = "✗"
        self.setText(f"{self.text} {status_icon}")
