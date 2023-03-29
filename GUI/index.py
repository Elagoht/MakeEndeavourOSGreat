#!/bin/env python3
from PyQt5.QtWidgets import QApplication
from sys import argv, exit
from MainWin import MainWin

app = QApplication(argv)
app.setApplicationName("Endeavour OS Tweaker")
main = MainWin()
exit(app.exec_())
