from PyQt5.QtWidgets import QWidget, QGroupBox, QPushButton, QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from Result import ResultWidget
from Utilities import run_command, install_if_doesnt_have, AppBox, GridBox


class DevelopmentTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create Devs section
        self.gbxDev = QGroupBox("Development packages", self)
        self.glyDev = QVBoxLayout(self.gbxDev)
        self.lblDev = QLabel(
            "Here are collections of development packages separated by languages for developers.")
        self.lblDev.setWordWrap(True)
        self.glyDev.addWidget(self.lblDev)

        # Common Utilities
        self.gbxCommon = GridBox("Common Apps")

        self.appVSCode = AppBox("VSCode", "visual-studio-code-bin")
        self.appCode = AppBox("Code", "code")
        self.appNeovim = AppBox("Neovim", "neovim")
        self.appEmacs = AppBox("Emacs", "emacs")
        self.appSqliteBrowser = AppBox(
            "DB Browser for SQLite", "sqlitebrowser")
        self.appMongoDB = AppBox("MongoDB", "mongodb-bin")
        self.appMariaDB = AppBox("MariaDB", "mariadb")

        self.gbxCommon.addWidget(self.appVSCode)
        self.gbxCommon.addWidget(self.appCode, 0, 1)
        self.gbxCommon.addWidgets(self.appNeovim,
                                  self.appEmacs,
                                  self.appSqliteBrowser,
                                  self.appMongoDB,
                                  self.appMariaDB)

        # HTML CSS
        self.gbxHTMLCSS = GridBox("HTML / CSS")
        self.appBlueFish = AppBox("BlueFish Editor", "bluefish")
        self.gbxHTMLCSS.addWidget(self.appBlueFish)

        # JavaScript
        self.gbxJavaScript = GridBox("JavaScript")
        self.appNodeJs = AppBox("Node.js", "nodejs")
        self.appNpm = AppBox("Npm", "npm")
        self.appYarn = AppBox("Yarn", "yarn")
        self.gbxJavaScript.addWidget(self.appNodeJs)
        self.gbxJavaScript.addWidget(self.appNpm, 0, 1)
        self.gbxJavaScript.addWidgets(self.appYarn)

        # Java
        self.gbxJava = GridBox("Java")
        self.appJDK = AppBox("JDK latest", "jdk-openjdk")
        self.appJDK17 = AppBox("JDK 17", "jdk17-openjdk")
        self.appJDK11 = AppBox("JDK 11", "jdk11-openjdk")
        self.appJDK8 = AppBox("JDK 8", "jdk8-openjdk")
        self.appEclipseJava = AppBox("Eclipse Java", "eclipse-java")
        self.gbxJava.addWidget(self.appJDK)
        self.gbxJava.addWidget(self.appJDK17, 0, 1)
        self.gbxJava.addWidgets(self.appJDK11,
                                self.appJDK8,
                                self.appEclipseJava)

        # Python
        self.gbxPython = GridBox("Python")
        self.appBpython = AppBox("bPython", "bpython")
        self.appIdle = AppBox("IDLE", "idle")
        self.appIdlex = AppBox("IDLEX", "idlex")
        self.appTk = AppBox("TK (for Tkinter)", "tk")
        self.gbxPython.addWidget(self.appBpython)
        self.gbxPython.addWidget(self.appIdle, 0, 1)
        self.gbxPython.addWidgets(self.appIdlex,
                                  self.appTk)

        # C#
        self.gbxCSharp = GridBox("C#")
        self.appDotnet = AppBox("Dotnet SDK", "dotnet-sdk")
        self.gbxCSharp.addWidget(self.appDotnet)

        # C/C++
        self.gbxCCpp = GridBox("C/C++")
        self.appCodeBlocks = AppBox("Code::Blocks", "codeblocks")
        self.appClion = AppBox("Clion", "clion")
        self.appEclipseCCpp = AppBox("Eclipse C/C++", "eclipse-cpp")
        self.appHeaders = AppBox("Linux Headers (.h files)", "linux-headers")
        self.appHeadersLts = AppBox("Linux LTS Headers", "linux-lts-headers")
        self.appHeadersZen = AppBox("Linux Zen Headers", "linux-zen-headers")
        self.gbxCCpp.addWidget(self.appCodeBlocks)
        self.gbxCCpp.addWidget(self.appClion, 0, 1)
        self.gbxCCpp.addWidgets(self.appEclipseCCpp,
                                self.appHeaders,
                                self.appHeadersLts,
                                self.appHeadersZen)

        # Rust
        self.gbxRust = GridBox("Rust")
        self.appRustUp = AppBox("RustUp", "rustup")
        self.gbxRust.addWidget(self.appRustUp)

        # R
        self.gbxR = GridBox("R")
        self.appR = AppBox("R", "r")
        self.appRStudio = AppBox("RStudio", "rstudio-desktop-bin")
        self.gbxR.addWidget(self.appR)
        self.gbxR.addWidget(self.appRStudio, 0, 1)

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxDev)
        self.layout.addWidget(self.gbxCommon)
        self.layout.addWidget(self.gbxHTMLCSS)
        self.layout.addWidget(self.gbxJavaScript)
        self.layout.addWidget(self.gbxJava)
        self.layout.addWidget(self.gbxPython)
        self.layout.addWidget(self.gbxCSharp)
        self.layout.addWidget(self.gbxCCpp)
        self.layout.addWidget(self.gbxRust)
        self.layout.addWidget(self.gbxR)
