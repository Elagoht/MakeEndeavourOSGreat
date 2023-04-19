from PyQt5.QtWidgets import QWidget, QGridLayout
from InnerWindow import SideWindow, TopBar, BottomBar
from SideBar import SideBar
from Welcome import WelcomeWin


class Central(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)

        self.barSide = SideBar(self)
        self.barTop = TopBar("Main Menu", self)
        self.barBottom = BottomBar(self)
        self.layWindow = QGridLayout()
        self.layWindow.addWidget(self.barTop, 0, 0)
        self.layWindow.addWidget(self.barBottom, 2, 0)

        # Add layouts and widgets to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.barSide, 0, 0, 3, 1)
        self.layout.addLayout(self.layWindow, 1, 1)

        # Initialize
        self.is_page_open = True
        self.close_window()

    # Close side window
    def close_window(self) -> None:
        try:
            self.winWidget.close()
            del self.winWidget
        except AttributeError:
            pass

        if self.is_page_open:
            self.winWidget = SideWindow(WelcomeWin, [self], self)
            self.layWindow.addWidget(self.winWidget, 1, 0)
            self.barTop.set_title("Main Menu")

        self.is_page_open = not self.is_page_open
        self.barSide.setVisible(not self.is_page_open)

    # Open side window
    def open_window(self, title: str, window_class: QWidget, params: list) -> None:
        self.close_window()
        self.winWidget = SideWindow(
            window_class, params if params else [], self, [])
        self.layWindow.addWidget(self.winWidget, 1, 0)
        self.barTop.set_title(title)
        self.barTop.toggle_back_button_visibility()
