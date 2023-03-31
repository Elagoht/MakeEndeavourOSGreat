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

        self.appCode = AppBox("Code", "code",
                              "GUI/Assets/Apps/code-oss.png",
                              "Code OSS, is a source-code editor made with the Electron Framework.")
        self.appVSCode = AppBox("VSCode", "visual-studio-code-bin",
                                "GUI/Assets/Apps/vscode.png",
                                "A Code OSS distribution with Microsoft specific customizations.")
        self.appNeovim = AppBox("Neovim", "neovim",
                                "GUI/Assets/Apps/nvim.png",
                                "Vim with lua scripting support and still supports vimscript.")
        self.appEmacs = AppBox("Emacs", "emacs",
                               "GUI/Assets/Apps/emacs.png",
                               "The extensible, customizable, self-documenting, real-time display editor.")
        self.appSqliteBrowser = AppBox("DB Browser for SQLite", "sqlitebrowser",
                                       "GUI/Assets/Apps/sqlitebrowser.png",
                                       "High quality visual tool to create, design and edit SQLite database.")
        self.appMongoDB = AppBox("MongoDB", "mongodb-bin",
                                 "GUI/Assets/Apps/mongodb.png",
                                 "Source-available, cross-platform, document-oriented NoSQL database program.")
        self.appMariaDB = AppBox("MariaDB", "mariadb",
                                 "GUI/Assets/Apps/mariadb.png",
                                 "Commercially supported fork of MySQL relational database management system.")

        self.gbxCommon.addWidget(self.appCode)
        self.gbxCommon.addWidget(self.appVSCode, 0, 1)
        self.gbxCommon.addWidget(self.appNeovim, 0, 2)
        self.gbxCommon.addWidgets(self.appEmacs,
                                  self.appSqliteBrowser,
                                  self.appMongoDB,
                                  self.appMariaDB)

        # HTML CSS
        self.gbxHTMLCSS = GridBox("HTML / CSS")
        self.appBlueFish = AppBox("BlueFish Editor", "bluefish",
                                  "GUI/Assets/Apps/bluefish.png",
                                  "Editor targeted for webdevelopers, with many options, scripts and programming code.")
        self.gbxHTMLCSS.addWidget(self.appBlueFish)

        # JavaScript
        self.gbxJavaScript = GridBox("JavaScript")
        self.appNodeJs = AppBox("Node.js", "nodejs",
                                "GUI/Assets/Apps/nodejs.png",
                                "Backend JavaScript runtime environment, executes JavaScript outside a web browser.")
        self.appNpm = AppBox("Npm", "npm",
                             "GUI/Assets/Apps/npm.png",
                             "Package manager for the JavaScript programming language.")
        self.appYarn = AppBox("Yarn", "yarn",
                              "GUI/Assets/Apps/yarn.png",
                              "Package manager for your code. It allows to use and share (e.g. JavaScript) code.")
        self.gbxJavaScript.addWidget(self.appNodeJs)
        self.gbxJavaScript.addWidget(self.appNpm, 0, 1)
        self.gbxJavaScript.addWidget(self.appYarn, 0, 2)

        # Java
        self.gbxJava = GridBox("Java")
        self.appJDK = AppBox("JDK latest", "jdk-openjdk",
                             "GUI/Assets/Apps/java.png",
                             "Java Development Kit by Oracle Corporation, latest version.")
        self.appJDK17 = AppBox("JDK 17", "jdk17-openjdk",
                               "GUI/Assets/Apps/java.png",
                               "Java Development Kit by Oracle Corporation, version 17.")
        self.appJDK11 = AppBox("JDK 11", "jdk11-openjdk",
                               "GUI/Assets/Apps/java.png",
                               "Java Development Kit by Oracle Corporation, version 11.")
        self.appJDK8 = AppBox("JDK 8", "jdk8-openjdk",
                              "GUI/Assets/Apps/java.png",
                              "Java Development Kit by Oracle Corporation, latest version 8.")
        self.appEclipseJava = AppBox("Eclipse Java", "eclipse-java",
                                     "GUI/Assets/Apps/eclipse.png",
                                     "Most popular integrated development environment for Java development.")
        self.gbxJava.addWidget(self.appJDK)
        self.gbxJava.addWidget(self.appJDK17, 0, 1)
        self.gbxJava.addWidget(self.appJDK11, 0, 2)
        self.gbxJava.addWidgets(self.appJDK8,
                                self.appEclipseJava)

        # Python
        self.gbxPython = GridBox("Python")
        self.appBpython = AppBox("bPython", "bpython",
                                 "GUI/Assets/Apps/bpython.png",
                                 "Fancy Python interpreter with syntax higlhligter and more.")
        self.appIdle = AppBox("IDLE", "idle",
                              "GUI/Assets/Apps/python.png",
                              "Integrated Development and Learning Environment for Python")
        self.appIdlex = AppBox("IDLEX", "idlex",
                               "GUI/Assets/Apps/python.png",
                               "Basically IDLE, extended.")
        self.appTk = AppBox("TK", "tk",
                            "GUI/Assets/Apps/tcltk.png",
                            "Graphical user interface toolkit. (Required for Tkinter)")
        self.gbxPython.addWidget(self.appBpython)
        self.gbxPython.addWidget(self.appIdle, 0, 1)
        self.gbxPython.addWidget(self.appIdlex, 0, 2)
        self.gbxPython.addWidgets(self.appTk)

        # C#
        self.gbxCSharp = GridBox("C#")
        self.appDotnet = AppBox("Dotnet SDK", "dotnet-sdk",
                                "GUI/Assets/Apps/dotnet.png",
                                "Software development kit to build and run .NET applications.")
        self.gbxCSharp.addWidget(self.appDotnet)

        # C/C++
        self.gbxCCpp = GridBox("C/C++")
        self.appCodeBlocks = AppBox("Code::Blocks", "codeblocks",
                                    "GUI/Assets/Apps/codeblocks.png",
                                    "IDE for multiple compilers including GCC, Clang and Visual C++.")
        self.appEclipseCCpp = AppBox("Eclipse C/C++", "eclipse-cpp",
                                     "GUI/Assets/Apps/eclipse.png",
                                     "The Eclipse CDT™ Project provides a fully functional C and C++.")
        self.appHeaders = AppBox("Linux Headers (.h files)", "linux-headers",
                                 "GUI/Assets/Apps/header.png",
                                 "Required header (*.h) files for Linux kernel.")
        self.appHeadersLts = AppBox("Linux LTS Headers", "linux-lts-headers",
                                    "GUI/Assets/Apps/header.png",
                                    "Required header (*.h) files for Linux LTS kernel.")
        self.appHeadersZen = AppBox("Linux Zen Headers", "linux-zen-headers",
                                    "GUI/Assets/Apps/header.png",
                                    "Required header (*.h) files for Linux ZEN kernel.")
        self.gbxCCpp.addWidget(self.appCodeBlocks)
        self.gbxCCpp.addWidget(self.appEclipseCCpp, 0, 1)
        self.gbxCCpp.addWidget(self.appHeaders, 0, 2)
        self.gbxCCpp.addWidgets(self.appHeadersLts,
                                self.appHeadersZen)

        # Rust
        self.gbxRust = GridBox("Rust")
        self.appRustUp = AppBox("RustUp", "rustup",
                                "GUI/Assets/Apps/rust.png",
                                "Installs The Rust Programming Language from the official release channels.")
        self.gbxRust.addWidget(self.appRustUp)

        # R
        self.gbxR = GridBox("R")
        self.appR = AppBox("R", "r",
                           "GUI/Assets/Apps/r.png",
                           "Programming language for statistical computing and graphics.")
        self.appRStudio = AppBox("RStudio", "rstudio-desktop-bin",
                                 "GUI/Assets/Apps/rstudio.png",
                                 "Integrated development environment for R.")
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
