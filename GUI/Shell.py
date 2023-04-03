from PyQt5.QtWidgets import QWidget, QGridLayout
from Utilities import ShellBox


class ShellTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create Bash section
        self.appBash = ShellBox("Bash (Default)",
                                "bash",
                                "GUI/Assets/Apps/bash.png",
                                "Unix shell and command language written for the GNU Project as a replacement for the Bourne shell. <font color='red'>Do not remove this package!</font>",
                                True
                                )

        # Create Shell section
        self.appSh = ShellBox("Sh",
                              "sh",
                              "GUI/Assets/Apps/sh.png",
                              "Shell command-line interpreter for computer operating systems. <font color='red'>Do not remove this package!</font>",
                              True
                              )

        # Create ZSH section
        self.appZsh = ShellBox("Zsh",
                               "zsh",
                               "GUI/Assets/Apps/zsh.png",
                               "extended Bourne shell with many improvements, including some features of Bash, ksh, and tcsh."
                               )

        # Create fish section
        self.appFish = ShellBox("Fish",
                                "fish",
                                "GUI/Assets/Apps/fish.png",
                                "Friendly interactive shell. Smart and user-friendly command line shell"
                                )

        # Insert groupboxes to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.appBash)
        self.layout.addWidget(self.appSh, 0, 1)
        self.layout.addWidget(self.appZsh)
        self.layout.addWidget(self.appFish)
