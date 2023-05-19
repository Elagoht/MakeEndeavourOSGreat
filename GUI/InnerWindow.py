from PyQt5.QtWidgets import QWidget, QScrollArea, QPushButton, QHBoxLayout, QLabel, QGridLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from Utilities import has_aur_helper, install_if_doesnt_have, uninstall_if_have, CommandButton
from typing import Iterable, Callable


class SideWindow(QScrollArea):
    def __init__(self, window_class: QWidget, params: list, parent: QWidget, close_actions: Iterable[Callable] = None) -> None:
        super().__init__()
        self.close_actions = close_actions if close_actions else []

        self.winWidget = window_class(*params)
        self.setWidget(self.winWidget)
        self.setWidgetResizable(True)
        self.setParent(parent)

    def close(self) -> bool:
        for action in self.close_actions:
            action()
        return super().close()


class TopBar(QWidget):
    def __init__(self, title: str, parent) -> None:
        super().__init__()
        self.setParent(parent)

        self.btnBack = QPushButton(QIcon("GUI/Assets/back.png"), "Back", self)
        self.lblTitle = QLabel(title)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.btnBack)
        self.layout.addWidget(self.lblTitle, 1)

        self.btnBack.clicked.connect(self.go_back)
        self.lblTitle.setAlignment(Qt.AlignCenter)

        # Initialize
        self.btnBack.hide()

    # Window title changer
    def set_title(self, new) -> None:
        self.lblTitle.setText(new)

    # Back to main page functin
    def go_back(self) -> None:
        self.parent().close_window()
        self.toggle_back_button_visibility()

    # Back button visibility setter
    def toggle_back_button_visibility(self) -> None:
        self.btnBack.setVisible(not self.btnBack.isVisible())


class BottomBar(QWidget):
    txtInstall = "To install: "
    txtUninstall = "To uninstall: "

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        # Install and uninstall lists
        self.to_install = []
        self.to_uninstall = []

        # Create "to install" and "to uninstall" lists
        self.lblInstall = QLabel(BottomBar.txtInstall, self)
        self.lblInstall.setWordWrap(True)
        self.lblUninstall = QLabel(BottomBar.txtUninstall, self)
        self.lblUninstall.setWordWrap(True)

        # Create apply button
        self.btnApply = CommandButton(
            QIcon("GUI/Assets/install.png"),
            "Apply",
            f"""{install_if_doesnt_have(" ".join(self.to_install))};
                {uninstall_if_have(" ".join(self.to_uninstall))}""",
            self,
            [
                lambda: self.clear_lists() if has_aur_helper() else QMessageBox.warning(
                    self, "AUR Helper Needed",
                    "To install all applications, you need an AUR helper. This program only supports paru and yay. You can install one with the help of this application."
                )
            ]
        )
        self.btnApply.setMaximumWidth(120)

        # Insert widgets to layout
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.lblInstall, 0, 0)
        self.layout.addWidget(self.lblUninstall, 1, 0)
        self.layout.addWidget(self.btnApply, 0, 1, 2, 1)

    # Handle installation list
    def to_install_list(self, package: str, checked: bool) -> None:
        if checked:
            if package not in self.to_install:
                self.to_install.append(package)
        elif package in self.to_install:
            self.to_install.remove(package)

        self.lblInstall.setText(
            BottomBar.txtInstall +
            "<font color=\"green\" face=\"monospace\">" +
            ", ".join(self.to_install) +
            "</font>"
        )
        self.update_thread_command()

    # Handle uninstallation list
    def to_uninstall_list(self, package: str, checked: bool) -> None:
        if checked:
            if package not in self.to_uninstall:
                self.to_uninstall.append(package)
        elif package in self.to_uninstall:
            self.to_uninstall.remove(package)

        self.lblUninstall.setText(
            BottomBar.txtUninstall +
            "<font color=\"red\" face=\"monospace\">" +
            ", ".join(self.to_uninstall) +
            "</font>"
        )
        self.update_thread_command()

    # * CummandButton is already connected as empty lists.
    # * To update command, update directly its command variable.
    def update_thread_command(self) -> None:
        self.btnApply.thread.command = \
            f"""{install_if_doesnt_have(" ".join(self.to_install)) if self.to_install else ""}
                {uninstall_if_have(" ".join(self.to_uninstall)) if self.to_uninstall else ""}
                """

    def clear_lists(self):
        self.to_install.clear()
        self.to_uninstall.clear()
        self.lblInstall.setText(BottomBar.txtInstall)
        self.lblUninstall.setText(BottomBar.txtUninstall)
