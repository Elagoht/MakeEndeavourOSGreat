from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPlainTextEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class TasksModal(QWidget):
    def __init__(self, install_list: list, uninstall_list: list):
        super().__init__()
        self.install_list = install_list
        self.uninstall_list = uninstall_list

        # Set window properties
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(480, 240)
        self.show()

        self.lblInstall = QLabel("Apps marked for installation")
        self.lstInstall = QPlainTextEdit(self)

        self.lblUninstall = QLabel("Apps marked for installation")
        self.lstUninstall = QPlainTextEdit(self)

        self.btnClose = QPushButton("Close", self)
        self.btnClose.clicked.connect(self.close)

        fontMono = QFont("monospace")
        self.lstInstall.setFont(fontMono)
        self.lstInstall.setReadOnly(True)
        self.lstInstall.setStyleSheet("color: green")
        self.lstUninstall.setFont(fontMono)
        self.lstUninstall.setReadOnly(True)
        self.lstUninstall.setStyleSheet("color: red")

        # Add widgets to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.lblInstall, 0, 0, 1, 4)
        self.layout.addWidget(self.lstInstall, 1, 0, 1, 4)
        self.layout.addWidget(self.lblUninstall, 2, 0, 1, 4)
        self.layout.addWidget(self.lstUninstall, 3, 0, 1, 4)
        self.layout.addWidget(self.btnClose, 4, 3, 1, 1)

        # Initialize
        self.update_install_list()
        self.update_uninstall_list()

    def update_install_list(self):
        self.lstInstall.setPlainText(
            ", ".join(self.install_list)
            if self.install_list
            else "Nothing to install"
        )

    def update_uninstall_list(self):
        self.lstUninstall.setPlainText(
            ", ".join(self.uninstall_list)
            if self.uninstall_list
            else "Nothing to uninstall"
        )
