from os import popen, system, WEXITSTATUS
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QGroupBox, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QThread, QProcess, pyqtSignal
from typing import Iterable
from json import load


class CommandButton(QPushButton):
    # Create a button to run commands in a separated thread
    def __init__(self, icon: QIcon, text: str, command: str, parent: QWidget, post_commands: Iterable[callable] = [], iconless: bool = False, avoid_xterm: bool = False) -> None:
        super().__init__()
        self.post_commands = post_commands
        self.avoid_xterm = avoid_xterm
        self.iconless = iconless
        self.setParent(parent)
        self.text = text
        self.setText(self.text)
        self.setIcon(icon)

        # Create command thread
        self.thread = CommandThread(command, avoid_xterm)
        self.clicked.connect(self.thread.start)
        self.thread.output.connect(self.on_thread_output)

    # Update button color and icon depending on exit status
    def set_status(self, status_code) -> None:
        if not self.iconless:
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
        # Run post-execute commands
        for command in self.post_commands:
            command()


class CommandThread(QThread):
    # Create thread worker for command button
    # Createa signal to communicate between threads
    output = pyqtSignal(int)

    def __init__(self, command, avoid_xterm) -> None:
        super().__init__()
        # Pass command to run method
        self.command = command
        self.avoid_xterm = avoid_xterm
    # Function will be executed on thread called

    def run(self) -> None:
        # Create bash process to run command
        process = QProcess()
        process.start("bash")
        # Write command to execute to bash standard input.
        process.write(f"""statusfile=$(mktemp);
        {"" if self.avoid_xterm else "xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T 'Endeavour OS Tweaker Slave' -bg black -fg peru -e"}\
        sh -c '{self.command}; echo $? > '$statusfile 2> /dev/null;
        cat $statusfile;
        rm $statusfile""".encode())
        process.closeWriteChannel()
        # Wait until process is finished.
        process.waitForFinished(-1)

        # Handle process's exit code.
        try:
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
        except RuntimeError:
            pass


class AppBox(QGroupBox):
    # Create app widget that have install management system
    def __init__(self, title: str, package: str, image: str, description: str, owner: QWidget, bar_bottom: QWidget, lists: Iterable[Iterable[str]] = [[], []]) -> None:
        super().__init__(owner)
        self.owner = owner
        self.package = package
        self.bar_bottom = bar_bottom
        self.is_installed: bool = False
        self.is_checked: bool = self.package in (
            *self.bar_bottom.to_install,
            *self.bar_bottom.to_uninstall
        )

        # Create layouts
        self.glyApp = QGridLayout(self)

        # Create info section
        self.lblTitle = QLabel("<b>" + title+" </b>")
        self.imgImage = QLabel(self)
        self.imgImage.setPixmap(QPixmap(image))
        self.imgImage.setFixedSize(64, 64)
        self.lblDescription = QLabel(description)
        # Make links clickable
        self.lblDescription.setOpenExternalLinks(True)
        self.lblDescription.setTextFormat(Qt.RichText)
        self.lblDescription.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.lblDescription.setWordWrap(True)
        self.btnInstall = AppInstallButton(
            self.is_installed, self.is_checked, self)
        self.btnInstall.setFixedSize(40, 40)

        # Description Box
        self.layDescription = QVBoxLayout()
        self.layDescription.addWidget(self.lblTitle)
        self.layDescription.addWidget(self.lblDescription)

        # Insert layouts and wigdets to layouts
        self.glyApp.addWidget(self.imgImage, 0, 0)
        self.glyApp.addLayout(self.layDescription, 0, 1)
        self.glyApp.addWidget(self.btnInstall, 0, 2)
        # Additional CSS
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")

        # Connect events
        self.btnInstall.clicked.connect(self.btnInstall.toggle_action)

        # Initialize
        self.btnInstall.update_install()


class AppInstallButton(QPushButton):
    # 4 state custom button for install managemenet
    def __init__(self, install_state: bool, action_state: bool, owner: AppBox):
        super().__init__("▼", owner)
        self.owner = owner
        self.install_state = install_state
        self.action_state = action_state

    def toggle_action(self):
        self.action_state = not self.action_state
        if self.install_state:
            if self.action_state:
                self.setStyleSheet(
                    """background: #b20;
                    border: 4px solid #a10;
                    padding:8px;
                    border-radius:6px;
                    color: white;"""
                )
                self.setText("×")
            else:
                self.setStyleSheet(
                    """background: #f68;
                    border: 4px solid #e57;
                    padding:8px;
                    border-radius:6px;
                    color: white;"""
                )
                self.setText("√")
            # Add to/Remove from "to uninstall" list
            self.owner.bar_bottom.to_uninstall_list(
                self.owner.package, not self.action_state)
        else:
            if self.action_state:
                self.setStyleSheet(
                    """background: #0a0;
                    border: 4px solid #090;
                    padding:8px;
                    border-radius:6px;
                    color: white;"""
                )
                self.setText("▼")
            else:
                self.setStyleSheet(
                    """background: #5d5;
                    border: 4px solid #4c4;
                    padding:8px;
                    border-radius:6px;
                    color: white;"""
                )
                self.setText("√")
            # Add to/Remove from "to install" list
            self.owner.bar_bottom.to_install_list(
                self.owner.package, not self.action_state)

    def check_install_state(self):
        return self.owner.package in self.owner.owner.installed_apps

    def update_install(self):
        self.install_state = self.check_install_state()
        self.toggle_action()


class ButtonBox(QGroupBox):
    # Create boxes can have multiple buttons
    def __init__(self, title: str, image: str, description: str, buttons: Iterable[QPushButton]) -> None:
        super().__init__()

        # Create layouts
        self.glyApp = QVBoxLayout(self)
        self.layInfo = QHBoxLayout()
        self.layButtons = QHBoxLayout()

        # Create information section
        self.lblTitle = QLabel("<b>" + title + "<b>")
        self.imgApp = QLabel(self)
        self.imgApp.setPixmap(QPixmap(image))
        self.imgApp.setFixedSize(64, 64)
        self.lblDescription = QLabel(description)
        self.lblDescription.setWordWrap(True)

        # Insert widgets to layout
        self.layInfo.addWidget(self.imgApp)
        self.layInfo.addWidget(self.lblDescription)
        for button in buttons:
            self.layButtons.addWidget(button)
        self.glyApp.addWidget(self.lblTitle)
        self.glyApp.addLayout(self.layInfo)
        self.glyApp.addStretch()
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
        super().__init__()
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
        super().__init__()
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

        super().__init__()
        self.package = package

        # Create layouts
        self.glyTheme = QVBoxLayout(self)
        self.layInfo = QGridLayout()
        self.layButtons = QGridLayout()

        # Create information section
        self.lblThemeTitle = QLabel(
            "<center><b>" + name + "</b></center>", self)
        self.lblThemeTitle.setWordWrap(True)
        self.imgTheme = QLabel(self)
        self.imgTheme.setPixmap(QPixmap(image))
        self.imgTheme.setFixedSize(64, 64)

        # Create installation buttons
        self.btnThemeInstall = CommandButton(
            QIcon("Assets/install.png"), "Install",
            install_if_doesnt_have(self.package),
            self, (self.check_install_state,), True)
        self.btnThemeUninstall = CommandButton(
            QIcon("Assets/uninstall.png"),
            "Uninstall",
            uninstall_if_have(self.package),
            self, (self.check_install_state,), True)

        # Insert layouts and widgets to layouts
        self.layInfo.addWidget(self.imgTheme, 0, 0, 2, 1)
        self.layInfo.addWidget(self.lblThemeTitle, 0, 1)
        self.glyTheme.addLayout(self.layInfo)
        self.glyTheme.addLayout(self.layButtons)
        self.glyTheme.addStretch()

        # Create list for theme-setter commandbuttons
        self.buttons = [CommandButton(
            QIcon("Assets/configure.png"), name,
            f"""[ "$(pacman -Qqs {self.package} | grep ^{self.package}$)" = "{self.package}" ] && \
            gsettings set org.gnome.desktop.interface {self.to_change} \"{theme + ("" if type != 3 else " 10")}\"""",
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

        # Initialize
        self.check_install_state()

    def check_install_state(self):
        # Get state
        name = self.package.split(" ")[0]
        is_installed = WEXITSTATUS(system(
            f"[ \"$(pacman -Qqs {name} | grep \"^{name}$\")\" = \"{name}\" ]"
        )) == 0
        # Insert/delete layouts and wigdets to layouts
        if is_installed:
            self.layInfo.removeWidget(self.btnThemeInstall)
            self.layInfo.addWidget(self.btnThemeUninstall, 1, 1)
            self.btnThemeInstall.hide()
            self.btnThemeUninstall.show()
        else:
            self.layInfo.removeWidget(self.btnThemeUninstall)
            self.layInfo.addWidget(self.btnThemeInstall, 1, 1)
            self.btnThemeInstall.show()
            self.btnThemeUninstall.hide()


class ShellBox(AppBox):
    # Create installable and uninstallable shell boxes that
    # support setting default shell for user and root
    def __init__(self, title: str, package: str, image: str, description: str, owner: QWidget, bottom_bar: QWidget, uninstallable: bool = False) -> None:
        super().__init__(title, package, image, description, owner, bottom_bar)

        # If uninstallable remove install buttons
        self.uninstallable = uninstallable
        if uninstallable:
            self.glyApp.removeWidget(self.btnInstall)
            del self.btnInstall

        # Setter buttons
        self.btnSet = CommandButton(
            QIcon("Assets/configure.png"), "Set Default",
            f"echo New shell will be {package}.;\
                [ \"{package}\" = \"sh\" ] || [ \"$(pacman -Qqs {package} | grep ^{package}$)\" = \"{package}\" ] &&\
                chsh -s /bin/{package}",
            self)
        self.btnSetRoot = CommandButton(
            QIcon("Assets/configure.png"), "Set Default for Root",
            f"echo New shell will be {package}.;\
                [ \"$(pacman -Qqs {package} | grep ^{package}$)\" = \"{package}\" ] && sudo chsh -s /bin/{package} root",
            self)

        # Add buttons to layout
        self.laySetButtons = QHBoxLayout()
        self.laySetButtons.addWidget(self.btnSet)
        self.laySetButtons.addWidget(self.btnSetRoot)
        self.glyApp.addLayout(self.laySetButtons, 2, 0, 1,
                              2 if self.uninstallable else 3)


class AppsWin(QWidget):
    # Create application install catalog window
    def __init__(self, json_file: str, owner: QWidget) -> None:
        super().__init__()
        self.setParent(owner)

        # Get installed apps list
        self.installed_apps = get_installed_apps()

        # Create layout
        self.layout = QVBoxLayout(self)

        # Read json file to get application data
        with open(json_file, "r") as programs_json:
            program_lists = load(programs_json)
        # Create and insert application boxes to layout
        for language_name, program_list in program_lists.items():
            grid_box = GridBox(language_name)
            for number, program in enumerate(program_list):
                if number < 2:
                    grid_box.addWidget(
                        AppBox(title=program["name"],
                               package=program["package"],
                               image=program["image"],
                               description=program["description"],
                               owner=self,
                               bar_bottom=self.parent().parent().parent().central_widget.barBottom),
                        0, number)
                else:
                    grid_box.glyField.addWidget(
                        AppBox(title=program["name"],
                               package=program["package"],
                               image=program["image"],
                               description=program["description"],
                               owner=self,
                               bar_bottom=self.parent().parent().parent().central_widget.barBottom))
            self.layout.addWidget(grid_box)
        self.layout.addStretch()


class DconfCheckBox(QCheckBox):
    # Create dconf setting checkbox
    def __init__(self, text, val: str) -> None:
        super().__init__(text)
        self.keybind = val

    @property
    def value(self):
        return self.keybind if self.isChecked() else ""


class DconfEditRow(QGroupBox):
    # Create dconf settings option
    def __init__(self, name: str, setting: str, checkboxes: Iterable[DconfCheckBox], is_list: bool = True) -> None:
        super().__init__()

        # Set properties
        self.checkboxes = checkboxes
        self.setting = setting
        self.is_list = is_list

        # Create Layouts
        self.lblDconf = QLabel(name)
        self.lblDconf.setAlignment(Qt.AlignTop)
        self.layout = QHBoxLayout(self)

        # Insert layouts and widgets to layouts
        self.layButtons = QGridLayout()
        self.layout.addWidget(self.lblDconf)
        self.layout.addLayout(self.layButtons)
        for number, checkbox in enumerate(self.checkboxes):
            if number < 2:
                self.layButtons.addWidget(checkbox, 0, number)
            else:
                self.layButtons.addWidget(checkbox)

        # Additional CSS
        self.setStyleSheet("""QGroupBox {
            background: rgba(0,0,0,.25);
            border: 1px solid rgba(0,0,0,.5);
            border-radius: .25em;
        }""")

        # Initialize
        self.check_current_state()

    # If already setted, check itself
    def check_current_state(self):
        # Get bindings from current configuration
        keybinds = [
            keybind.strip() for keybind in
            popen("gsettings get " + self.setting)
            .read().strip()[1:-1].split(",")
        ]

        for checkbox in self.checkboxes:
            checkbox.setChecked(checkbox.keybind in keybinds)

    # Create command property
    @property
    def command(self):
        return "gsettings set " + \
            self.setting + " \"" + \
            ("[" if self.is_list else "") + \
            (", ".join([
                option for option in
                list(filter(
                    lambda val: val != "",
                    [checkbox.value for checkbox in self.checkboxes]
                ))
            ])) + \
            ("]" if self.is_list else "") + \
            "\""


class DconfEditBox(QGroupBox):
    # Create dconf settings editor
    def __init__(self, title: str, options: Iterable[DconfEditRow]) -> None:
        super().__init__(title)
        self.settings = []
        self.txtDconf = "Save Changes"

        # Insert widgets to layout
        self.glyDconf = QVBoxLayout(self)
        self.add_options(*options)

        # Create widgets
        self.btnDconf = QPushButton(
            QIcon("Assets/configure.png"), self.txtDconf, self)
        self.glyDconf.addWidget(self.btnDconf)

        # Connect buttons to functions
        self.btnDconf.clicked.connect(lambda: self.save_changes())

    # Define add option function
    def add_options(self, *options: Iterable[DconfEditRow]):
        for option in options:
            self.settings.append(option)
            self.glyDconf.addWidget(option)

    # Define save changes
    def save_changes(self):
        command = "\n".join(setting.command for setting in self.settings)
        exit_status = WEXITSTATUS(system(command))
        match exit_status:
            case 0:
                self.btnDconf.setText(self.txtDconf + "✓")
                self.btnDconf.setStyleSheet("color: green")
            case _:
                self.btnDconf.setStyleSheet("color: red")
                self.btnDconf.setText(self.txtDconf + "✗")


class MonoFont(QFont):
    # Create terminal font
    def __init__(self) -> None:
        super().__init__("Monospace")
        self.setPointSize(12)
        self.setStyleHint(QFont.Monospace)


class CommandLine(QTextEdit):
    # Create terminal output
    def __init__(self, text, height) -> None:
        super().__init__()
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
            aurhelper="/bin/paru --noconfirm --skipreview"
        elif [ "$(command -v yay)" ]; then
            aurhelper="sudo /bin/yay --noeditmenu --nodiffmenu --norebuild --noredownload --nopgpfetch"
        else
            aurhelper="/bin/sudo /bin/pacman"
        fi
        echo $aurhelper"""
    ).readline().strip()


def has_aur_helper() -> bool:
    # Check if have aur helper
    return aur_helper() != "/bin/sudo /bin/pacman"


def install_if_doesnt_have(package: str) -> str:
    # If app is already installed, do not try to install again, else install
    # Returns string to use on command texts
    # Checks aur helper and inserts required parameters.
    name = package.split(" ")[0]
    return f"""if [ ! "$(pacman -Qqs {name} | grep "^{name}$")" = "{name}" ]
        then {aur_helper()} -S {name}
    fi""" if has_aur_helper() else "false"


def uninstall_if_have(package: str) -> str:
    # If app is not already installed, do not try to uninstall again, else uninstall
    # Returns string to use on command texts
    name = package.split(" ")[0]
    return f"""if [ "$(pacman -Qqs {name} | grep "^{name}$" )" = "{name}" ]
        then {aur_helper()} -R {name}
    fi""" if has_aur_helper() else "false"


def color(color: str, text: str) -> str:
    # Return colored text for labels
    return f"<font color='{color}'>{text}</font>"


def long_bash_script(file: str) -> str:
    with open(file, "r", encoding="UTF-8") as code:
        return code.read()


def get_installed_apps() -> list:
    return popen("pacman -Qq").read().splitlines()
