from PyQt5.QtWidgets import QWidget, QScrollArea, QPushButton, QHBoxLayout, QLabel, QGridLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from Tasks import TasksModal
from Utilities import has_aur_helper, aur_helper, CommandButton
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
        self.btnBack.hide()


class BottomBar(QWidget):

    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        # Install and uninstall lists
        self.to_install = []
        self.to_uninstall = []
        self.tasks = "{} to install, {} to remove."

        # Create "to install" and "to uninstall" lists
        self.lblTask = QLabel(self.tasks.format(0, 0), self)

        # Create tasks window opener
        self.btnTasks = QPushButton("Tasks", self)
        # TODO: Add tasks window open code
        self.btnTasks.clicked.connect(self.open_tasks_modal)
        # Create apply button
        self.btnApply = CommandButton(
            QIcon("GUI/Assets/install.png"),
            "Apply",
            "",
            self,
            [
                lambda: self.clear_lists() if has_aur_helper() else QMessageBox.warning(
                    self, "AUR Helper Needed",
                    "To install all applications, you need an AUR helper. This program only supports paru and yay. You can install one with the help of this application."
                ),
                self.parent().close_window
            ],
            True
        )
        self.btnApply.setMaximumWidth(120)
        self.btnTasks.setMaximumWidth(120)

        # Insert widgets to layout
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.lblTask, 0, 0)
        self.layout.addWidget(self.btnTasks, 0, 1)
        self.layout.addWidget(self.btnApply, 0, 2)

        # Initialize
        self.update_button_availablity()

    # Handle installation list
    def to_install_list(self, package: str, checked: bool) -> None:
        if checked:
            if package not in self.to_install:
                self.to_install.append(package)
        elif package in self.to_install:
            self.to_install.remove(package)

        self.lblTask.setText(self.tasks.format(
            len(self.to_install),
            len(self.to_uninstall)
        ))
        self.update_button_availablity()
        self.update_thread_command()

    # Handle uninstallation list
    def to_uninstall_list(self, package: str, checked: bool) -> None:
        if checked:
            if package not in self.to_uninstall:
                self.to_uninstall.append(package)
        elif package in self.to_uninstall:
            self.to_uninstall.remove(package)

        self.lblTask.setText(self.tasks.format(
            len(self.to_install),
            len(self.to_uninstall)
        ))
        self.update_button_availablity()
        self.update_thread_command()

    def update_button_availablity(self):
        self.btnApply.setEnabled(
            any([self.to_install, self.to_uninstall]))
        self.btnTasks.setEnabled(
            any([self.to_install, self.to_uninstall]))

    # * CummandButton is already connected as empty lists.
    # * To update command, update directly its command variable.
    def update_thread_command(self) -> None:
        self.btnApply.thread.command = \
            f"""{(aur_helper() + " -S " + " ".join(self.to_install)) if self.to_install else ""}
                {(aur_helper() + " -R " + " ".join(self.to_uninstall)) if self.to_uninstall else ""}
                """

    def clear_lists(self):
        self.to_install.clear()
        self.to_uninstall.clear()
        self.lblTask.setText(self.tasks.format(
            len(self.to_install),
            len(self.to_uninstall)
        ))

    def open_tasks_modal(self):
        self.modal = TasksModal(self.to_install, self.to_uninstall)
