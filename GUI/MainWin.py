from PyQt5.QtWidgets import QApplication, QFileDialog, QLineEdit, QMainWindow, QSpinBox, QWidget, QGroupBox, QPushButton, QLabel, QGridLayout, QStatusBar
from PyQt5.QtGui import QKeySequence
from Central import Central


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.show()
        self.setMinimumWidth(400)
        self.l_status = QStatusBar()
        self.setStatusBar(self.l_status)
        self.central = Central()
        self.setCentralWidget(self.central)
