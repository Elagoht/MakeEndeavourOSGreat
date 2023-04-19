from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from Central import Central


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = Central(self)
        self.setCentralWidget(self.central_widget)
        self.setMinimumSize(900, 500)
        self.show()

    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
