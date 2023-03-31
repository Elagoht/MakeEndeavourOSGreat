from PyQt5.QtWidgets import QMainWindow
from Central import Central


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.central = Central()
        self.setCentralWidget(self.central)
        self.setMinimumSize(900, 500)
        self.show()
