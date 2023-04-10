from PyQt5.QtWidgets import QWidget, QScrollArea, QPushButton, QHBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from typing import Iterable, Callable


class SideWindow(QScrollArea):
    def __init__(self, window_class: QWidget, params: list, parent: QWidget, close_actions: Iterable[Callable] = []) -> None:
        super(QScrollArea, self).__init__()
        self.close_actions = close_actions

        self.winWidget = window_class(*params)
        self.setWidget(self.winWidget)
        self.setWidgetResizable(True)
        self.setParent(parent)
        # self.setMinimumSize(900, 500)

    def close(self) -> bool:
        for action in self.close_actions:
            action()
        return super().close()


class TopBar(QWidget):
    def __init__(self, title: str, parent) -> None:
        super(QWidget, self).__init__()
        self.setParent(parent)

        self.btnBack = QPushButton(QIcon("GUI/Assets/back.png"), "", self)
        self.lblTitle = QLabel(title)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.btnBack)
        self.layout.addWidget(self.lblTitle, 1)

        self.btnBack.clicked.connect(self.go_back)
        self.lblTitle.setAlignment(Qt.AlignCenter)

        # Initialize
        self.btnBack.hide()

    def set_title(self, new) -> None:
        self.lblTitle.setText(new)

    def go_back(self) -> None:
        self.parent().close_window()
        self.toggle_back_button_visibility()

    def toggle_back_button_visibility(self) -> None:
        self.btnBack.setVisible(not self.btnBack.isVisible())


class BottomBar(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        # Install and uninstall lists
        self.to_install = []
        self.to_uninstall = []

        txtInstall = "To install: "
        txtUninstall = "To uninstall: "

        self.lblInstall = QLabel(txtInstall, self)
        self.lblUninstall = QLabel(txtUninstall, self)
        self.btnInstall = QPushButton(
            QIcon("GUI/Assets/install.png"), "Start", self)
        self.btnInstall.setMaximumWidth(120)

        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.lblInstall, 0, 0)
        self.layout.addWidget(self.lblUninstall, 1, 0)
        self.layout.addWidget(self.btnInstall, 0, 1, 2, 1)

    # Add to install list if not already exists

    def add_to_install(self, package: str) -> None:
        if package not in self.to_install:
            self.to_install.append(package)
        self.lblInstall.setText(", ".join([self.to_install]))

    # Add to uninstall list if not already exists
    def add_to_uninstall(self, package: str) -> None:
        if package not in self.to_uninstall:
            self.to_uninstall.append(package)
            self.lblUninstall.setText(", ".join([self.to_uninstall]))
