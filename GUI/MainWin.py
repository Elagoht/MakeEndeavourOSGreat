from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from Central import Central


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.central = Central(self)
        self.setCentralWidget(self.central)
        self.setFixedSize(500, 275)
        self.show()

    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
