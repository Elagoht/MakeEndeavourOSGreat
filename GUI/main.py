#!/bin/env python3
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from sys import argv, exit
from MainWin import MainWin

app = QApplication(argv)
app.setApplicationName("eos-tweaker")
app.setApplicationDisplayName("Endeavour OS Tweaker")
app.setApplicationVersion("v0.2")
app.setStyle("kvantum")
app.setWindowIcon(QIcon("Assets/icon.png"))
main = MainWin()
exit(app.exec_())
