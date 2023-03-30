from PyQt5.QtWidgets import QWidget, QGroupBox, QLabel, QVBoxLayout
from Utilities import AppBox, GridBox


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

        self.appVSCode = AppBox("VSCode", "visual-studio-code-bin",
                                "GUI/Assets/Apps/vscode.png")
        self.appCode = AppBox("Code", "code",
                              "GUI/Assets/Apps/code-oss.png")
        self.appNeovim = AppBox("Neovim", "neovim",
                                "GUI/Assets/Apps/nvim.png")
        self.appEmacs = AppBox("Emacs", "emacs",
                               "GUI/Assets/Apps/emacs.png")
        self.appSqliteBrowser = AppBox("DB Browser for SQLite", "sqlitebrowser",
                                       "GUI/Assets/Apps/sqlitebrowser.png")
        self.appMongoDB = AppBox("MongoDB", "mongodb-bin",
                                 "GUI/Assets/Apps/mongodb.png")
        self.appMariaDB = AppBox("MariaDB", "mariadb",
                                 "GUI/Assets/Apps/mariadb.png")

        self.gbxCommon.addWidget(self.appVSCode)
        self.gbxCommon.addWidget(self.appCode, 0, 1)
        self.gbxCommon.addWidget(self.appNeovim, 0, 2)
        self.gbxCommon.addWidgets(self.appEmacs,
                                  self.appSqliteBrowser,
                                  self.appMongoDB,
                                  self.appMariaDB)

        # HTML CSS
        self.gbxHTMLCSS = GridBox("HTML / CSS")
        self.appBlueFish = AppBox("BlueFish Editor", "bluefish",
                                  "GUI/Assets/Apps/bluefish.png")
        self.gbxHTMLCSS.addWidget(self.appBlueFish)

        # JavaScript
        self.gbxJavaScript = GridBox("JavaScript")
        self.appNodeJs = AppBox("Node.js", "nodejs",
                                "GUI/Assets/Apps/nodejs.png")
        self.appNpm = AppBox("Npm", "npm",
                             "GUI/Assets/Apps/npm.png")
        self.appYarn = AppBox("Yarn", "yarn",
                              "GUI/Assets/Apps/yarn.png")
        self.gbxJavaScript.addWidget(self.appNodeJs)
        self.gbxJavaScript.addWidget(self.appNpm, 0, 1)
        self.gbxJavaScript.addWidget(self.appYarn, 0, 2)

        # Java
        self.gbxJava = GridBox("Java")
        self.appJDK = AppBox("JDK latest", "jdk-openjdk",
                             "GUI/Assets/Apps/java.png")
        self.appJDK17 = AppBox("JDK 17", "jdk17-openjdk",
                               "GUI/Assets/Apps/java.png")
        self.appJDK11 = AppBox("JDK 11", "jdk11-openjdk",
                               "GUI/Assets/Apps/java.png")
        self.appJDK8 = AppBox("JDK 8", "jdk8-openjdk",
                              "GUI/Assets/Apps/java.png")
        self.appEclipseJava = AppBox("Eclipse Java", "eclipse-java",
                                     "GUI/Assets/Apps/eclipse.png")
        self.gbxJava.addWidget(self.appJDK)
        self.gbxJava.addWidget(self.appJDK17, 0, 1)
        self.gbxJava.addWidget(self.appJDK11, 0, 2)
        self.gbxJava.addWidgets(self.appJDK8,
                                self.appEclipseJava)

        # Python
        self.gbxPython = GridBox("Python")
        self.appBpython = AppBox("bPython", "bpython",
                                 "GUI/Assets/Apps/bpython.png")
        self.appIdle = AppBox("IDLE", "idle",
                              "GUI/Assets/Apps/python.png")
        self.appIdlex = AppBox("IDLEX", "idlex",
                               "GUI/Assets/Apps/python.png")
        self.appTk = AppBox("TK (for Tkinter)", "tk",
                            "GUI/Assets/Apps/tcltk.png")
        self.gbxPython.addWidget(self.appBpython)
        self.gbxPython.addWidget(self.appIdle, 0, 1)
        self.gbxPython.addWidget(self.appIdlex, 0, 2)
        self.gbxPython.addWidgets(self.appTk)

        # C#
        self.gbxCSharp = GridBox("C#")
        self.appDotnet = AppBox("Dotnet SDK", "dotnet-sdk",
                                "GUI/Assets/Apps/dotnet.png")
        self.gbxCSharp.addWidget(self.appDotnet)

        # C/C++
        self.gbxCCpp = GridBox("C/C++")
        self.appCodeBlocks = AppBox("Code::Blocks", "codeblocks",
                                    "GUI/Assets/Apps/codeblocks.png")
        self.appClion = AppBox("Clion", "clion",
                               "GUI/Assets/Apps/clion.png")
        self.appEclipseCCpp = AppBox("Eclipse C/C++", "eclipse-cpp",
                                     "GUI/Assets/Apps/eclipse.png")
        self.appHeaders = AppBox("Linux Headers (.h files)", "linux-headers",
                                 "GUI/Assets/Apps/header.png")
        self.appHeadersLts = AppBox("Linux LTS Headers", "linux-lts-headers",
                                    "GUI/Assets/Apps/header.png")
        self.appHeadersZen = AppBox("Linux Zen Headers", "linux-zen-headers",
                                    "GUI/Assets/Apps/header.png")
        self.gbxCCpp.addWidget(self.appCodeBlocks)
        self.gbxCCpp.addWidget(self.appClion, 0, 1)
        self.gbxCCpp.addWidget(self.appEclipseCCpp, 0, 2)
        self.gbxCCpp.addWidgets(self.appHeaders,
                                self.appHeadersLts,
                                self.appHeadersZen)

        # Rust
        self.gbxRust = GridBox("Rust")
        self.appRustUp = AppBox("RustUp", "rustup",
                                "GUI/Assets/Apps/rust.png")
        self.gbxRust.addWidget(self.appRustUp)

        # R
        self.gbxR = GridBox("R")
        self.appR = AppBox("R", "r",
                           "GUI/Assets/Apps/r.png")
        self.appRStudio = AppBox("RStudio", "rstudio-desktop-bin",
                                 "GUI/Assets/Apps/rstudio.png")
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
