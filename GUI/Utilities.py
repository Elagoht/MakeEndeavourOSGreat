from os import popen, system, WEXITSTATUS
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QGroupBox, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QThread, QProcess, pyqtSignal
from typing import Iterable
from json import load


class CommandButton(QPushButton):
    # Create a button to run commands in a separated thread
    def __init__(self, icon: QIcon, text: str, command: str, parent: QWidget) -> None:
        super(QPushButton, self).__init__()
        self.setParent(parent)
        self.text = text
        self.setText(self.text)
        self.setIcon(icon)

        # Create command thread
        self.thread = CommandThread(command)
        self.clicked.connect(self.thread.start)
        self.thread.output.connect(self.on_thread_output)

    # Update button color and icon depending on exit status
    def set_status(self, status_code) -> None:
        status_icon = ""
        match status_code:
            case 0:
                self.setStyleSheet("color: green")
                status_icon = "✓"
            case -1:
                # Special exit code that means terminal closed by user.
                self.setStyleSheet("color: gray")
                status_icon = "☠"
            case _:
                self.setStyleSheet("color: red")
                status_icon = "✗"
        self.setText(f"{self.text} {status_icon}")

    # Function will be called after thread end
    def on_thread_output(self, status_code) -> None:
        self.set_status(status_code)


class CommandThread(QThread):
    # Create thread worker for command button

    # Createa signal to communicate between threads
    output = pyqtSignal(int)

    def __init__(self, command) -> None:
        super().__init__()

        # Pass command to run method
        self.command = command

    # Function will be executed on thread called
    def run(self) -> None:
        # Create bash process to run command
        process = QProcess()
        process.start("bash")
        # Write command to execute to bash standard input.
        process.write(f"""statusfile=$(mktemp);
        xterm -bg black -fg green -e sh -c '{self.command}; echo $? > '$statusfile 2> /dev/null;
        cat $statusfile;
        rm $statusfile""".encode())
        process.closeWriteChannel()
        # Wait until process is finished.
        process.waitForFinished()

        # Handle process's exit code.
        status_code = process.readAllStandardOutput()\
            .data().decode()
        if status_code != "":
            status_code = status_code.splitlines()[-1]
        else:
            status_code = 1
        try:
            status_code = int(status_code)
        except ValueError:
            # If exit code couldn't get, set as special exit code
            status_code = -1
        self.output.emit(status_code)


class AppBox(QGroupBox):
    # Create app widget that have install management system
    def __init__(self, title: str, package: str, image: str, description: str) -> None:
        super(QGroupBox, self).__init__()

        # Create layouts
        self.glyApp = QVBoxLayout(self)
        self.layButtons = QHBoxLayout()

        # Create info section
        self.lblTitle = QLabel("<b>" + title + "<b>")
        # * Placing table because Qt supports float only for images and tables and cannot add padding
        self.lblDescription = QLabel(
            f"""
            <table style="float: left;">
                <tr>
                    <td width="136" height="136">
                        <img src="{image}" />
                    </td>
                </tr>
            </table>
            <span>
                {description}
            </span>""")
        # Make links clickable
        self.lblDescription.setOpenExternalLinks(True)
        self.lblDescription.setTextFormat(Qt.RichText)
        self.lblDescription.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.lblDescription.setWordWrap(True)

        # Create ınstallation buttons
        self.btnInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install",
            install_if_doesnt_have(package), self)
        self.btnUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall",
            uninstall_if_have(package), self)

        # Insert layouts and wigdets to layouts
        self.layButtons.addWidget(self.btnInstall)
        self.layButtons.addWidget(self.btnUninstall)
        self.glyApp.addWidget(self.lblTitle)
        self.glyApp.addWidget(self.lblDescription)
        self.glyApp.addStretch()
        self.glyApp.addLayout(self.layButtons)
        # Additional CSS
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")


class ButtonBox(QGroupBox):
    # Create boxes can have multiple buttons
    def __init__(self, title: str, image: str, description: str, buttons: Iterable[QPushButton]) -> None:
        super(QGroupBox, self).__init__()

        # Create layouts
        self.glyApp = QVBoxLayout(self)
        self.layInfo = QHBoxLayout()
        self.layButtons = QHBoxLayout()

        # Create information section
        self.lblTitle = QLabel("<b>" + title + "<b>")
        self.imgApp = QLabel(self)
        self.imgApp.setPixmap(QPixmap(image))
        self.imgApp.setFixedSize(128, 128)
        self.lblDescription = QLabel(description)
        self.lblDescription.setWordWrap(True)

        # Insert widgets to layout
        self.layInfo.addWidget(self.imgApp)
        self.layInfo.addWidget(self.lblDescription)
        for button in buttons:
            self.layButtons.addWidget(button)
        self.glyApp.addWidget(self.lblTitle)
        self.glyApp.addLayout(self.layInfo)
        self.glyApp.addLayout(self.layButtons)

        # Additional CSS
        self.setStyleSheet("""QGroupBox {
            background: rgba(0, 0, 0, .25);
            border: 1px solid rgba(0, 0, 0, .5);
            border-radius: .25em;
        }""")


class GridBox(QGroupBox):
    # Create an easy to use groupbox, gridlayout combination
    def __init__(self, title: str) -> None:
        super(QGroupBox, self).__init__()
        self.setTitle(title)
        self.glyField = QGridLayout(self)

    # Define widget add functions to pass it to gridlayout
    def addWidget(self, widget: QWidget, row: int = 0, col: int = 0, rSpan: int = 1, cSpan: int = 1) -> None:
        self.glyField.addWidget(widget, row, col, rSpan, cSpan)
        for column in range(self.glyField.columnCount()):
            self.glyField.setColumnStretch(column, 1)

    def addWidgets(self, *widgets: QWidget) -> None:
        for widget in widgets:
            self.glyField.addWidget(widget)
        for column in range(self.glyField.columnCount()):
            self.glyField.setColumnStretch(column, 1)


class ExtensionBox(QGroupBox):
    # Create a smaller box for extensions with only image and clickable link.
    def __init__(self, title: str, link: str, image: str) -> None:
        super(QGroupBox, self).__init__()
        self.glyExt = QHBoxLayout(self)

        # Create image
        self.imgExt = QLabel(self)
        self.imgExt.setPixmap(QPixmap(image))
        self.imgExt.setFixedWidth(36)
        # Create clickable link
        self.lblExt = QLabel(
            f"< a href=\"{link}\" style=\"text-decoration: none; color:cornflowerblue\">{title}</a>")
        self.lblExt.setWordWrap(True)
        self.lblExt.setOpenExternalLinks(True)
        self.lblExt.setTextInteractionFlags(Qt.TextBrowserInteraction)

        # Insert widgets to layout
        self.glyExt.addWidget(self.imgExt)
        self.glyExt.addWidget(self.lblExt)

        # Additional CSS
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")


class ThemeBox(QGroupBox):
    # Create a box for themes that have theme setter buttons unlike appbox
    def __init__(self, name: str, package: str, image: str, themes: dict, type: int = 0) -> None:
        """
        type 0 = GTK Theme
        type 1 = Icon Theme
        type 2 = Cursor Theme
        type 3 = Monospace Font
        """
        # Determine theme type
        match type:
            case 1:
                self.to_change = "icon-theme"
            case 2:
                self.to_change = "cursor-theme"
            case 3:
                self.to_change = "monospace-font-name"
            case _:
                self.to_change = "gtk-theme"

        super(QGroupBox, self).__init__()

        # Create layouts
        self.glyTheme = QVBoxLayout(self)
        self.layInfo = QGridLayout()
        self.layButtons = QGridLayout()

        # Create information section
        self.lblThemeTitle = QLabel("<b>" + name + "</b>", self)
        self.lblThemeTitle.setWordWrap(True)
        self.imgTheme = QLabel(self)
        self.imgTheme.setPixmap(QPixmap(image))
        self.imgTheme.setFixedSize(128, 128)

        # Create installation buttons
        self.btnThemeInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install",
            install_if_doesnt_have(package),
            self)
        self.btnThemeUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"),
            "Uninstall",
            uninstall_if_have(package),
            self)

        # Insert layouts and widgets to layouts
        self.layInfo.addWidget(self.imgTheme, 0, 0, 3, 1)
        self.layInfo.addWidget(self.lblThemeTitle, 0, 1)
        self.layInfo.addWidget(self.btnThemeInstall, 1, 1)
        self.layInfo.addWidget(self.btnThemeUninstall, 2, 1)
        self.glyTheme.addLayout(self.layInfo)
        self.glyTheme.addLayout(self.layButtons)
        self.glyTheme.addStretch()

        # Create list for theme-setter commandbuttons
        self.buttons = [CommandButton(
            QIcon("GUI/Assets/configure.png"), name,
            f"""[ "$(pacman -Qqs {package} | grep ^{package}$)" = "{package}" ] && \
            gsettings set org.gnome.desktop.interface {self.to_change} '{theme}'""",
            self)
            for name, theme in themes.items()
        ]

        # Add buttons to buttons layout
        for number, button in enumerate(self.buttons):
            if number == 1:
                self.layButtons.addWidget(button, 0, 1)
            else:
                self.layButtons.addWidget(button)

        # Additional CSS
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")


class ShellBox(AppBox):
    # Create installable and uninstallable shell boxes that
    # support setting default shell for user and root
    def __init__(self, title: str, package: str, image: str, description: str, uninstallable: bool = False) -> None:
        super().__init__(title, package, image, description)

        # If uninstallable remove install buttons
        if uninstallable:
            self.glyApp.removeWidget(self.btnInstall)
            self.glyApp.removeWidget(self.btnUninstall)
            del self.btnInstall
            del self.btnUninstall

        # Setter buttons
        self.btnSet = CommandButton(
            QIcon("GUI/Assets/configure.png"), "Set Default",
            f"echo New shell will be {package}.;\
                [ \"{package}\" = \"sh\" ] || [ \"$(pacman -Qqs {package} | grep ^{package}$)\" = \"{package}\" ] &&\
                chsh -s /bin/{package}",
            self)
        self.btnSetRoot = CommandButton(
            QIcon("GUI/Assets/configure.png"), "Set Default for Root",
            f"echo New shell will be {package}.;\
                [ \"$(pacman -Qqs {package} | grep ^{package}$)\" = \"{package}\" ] && sudo chsh -s /bin/{package} root",
            self)

        # Add buttons to layout
        self.laySetButtons = QHBoxLayout()
        self.laySetButtons.addWidget(self.btnSet)
        self.laySetButtons.addWidget(self.btnSetRoot)
        self.glyApp.addLayout(self.laySetButtons)


class AppsWin(QWidget):
    # Create application install catalog window
    def __init__(self, json_file: str) -> None:
        super(QWidget, self).__init__()

        # Create layout
        self.layout = QVBoxLayout(self)

        # Read json file to get application data
        with open(json_file, "r") as programs_json:
            program_lists = load(programs_json)
        # Create and insert application boxes to layout
        for language_name, program_list in program_lists.items():
            grid_box = GridBox(language_name)
            for number, program in enumerate(program_list):
                match number:
                    case 1:
                        grid_box.addWidget(AppBox(*program), 0, 1)
                    case 2:
                        grid_box.addWidget(AppBox(*program), 0, 2)
                    case _:
                        grid_box.glyField.addWidget(AppBox(*program))
            self.layout.addWidget(grid_box)


class MonoFont(QFont):
    # Create terminal font
    def __init__(self) -> None:
        super(QFont, self).__init__("Monospace")
        self.setPointSize(12)
        self.setStyleHint(QFont.Monospace)


class CommandLine(QTextEdit):
    # Create terminal output
    def __init__(self, text, height) -> None:
        super(QTextEdit, self).__init__()
        self.setText(text)
        self.setFont(MonoFont())
        self.setFixedHeight(height)
        self.setReadOnly(True)
        self.setStyleSheet(
            """QTextEdit {
                background: black;
            }""")


def aur_helper() -> str:
    # Get AUR helper
    return popen(
        """if [ "$(command -v paru)" ]; then
            aurhelper="/bin/paru"
        elif [ "$(command -v yay)" ]; then
            aurhelper="/bin/yay"
        else
            aurhelper=""
        fi
        echo $aurhelper"""
    ).readline().strip()


def has_aur_helper() -> bool:
    # Check if have aur helper
    return aur_helper() != ""


def install_if_doesnt_have(package: str) -> str:
    # If app is already installed, do not try to install again, else install
    # Returns string to use on command texts
    return f"""if [ ! "$(pacman -Qqs {package} | grep "^{package}$")" = "{package}" ]
        then {aur_helper()} -S {package}
    fi""" if has_aur_helper() else "false"


def uninstall_if_have(package: str) -> str:
    # If app is not already installed, do not try to uninstall again, else uninstall
    # Returns string to use on command texts
    return f"""if [ "$(pacman -Qqs {package} | grep "^{package}$" )" = "{package}" ]
        then {aur_helper()} -R {package}
    fi""" if has_aur_helper() else "false"


def color(color: str, text: str) -> str:
    # Return colored text for labels
    return f"<font color='{color}'>{text}</font>"
