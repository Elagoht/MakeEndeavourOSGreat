#!/bin/env python3
from PyQt5.QtWidgets import QApplication
from sys import argv
from MainWin import MainWin

app = QApplication(argv)
app.setApplicationName("eos-tweaker")
app.setApplicationDisplayName("Endeavour OS Tweaker")
app.setApplicationVersion("v0.2")
app.setStyle("kvantum")
main = MainWin()
exit(app.exec_())
