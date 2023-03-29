from PyQt5.QtWidgets import QMainWindow, QStatusBar
from PyQt5.QtGui import QKeySequence
from Central import Central


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.show()
        self.l_status = QStatusBar()
        self.setStatusBar(self.l_status)
        self.central = Central()
        self.setCentralWidget(self.central)
        self.setMinimumSize(600, 400)
