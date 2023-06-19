from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from Utilities import ShellBox, ButtonBox, CommandButton, long_bash_script, get_installed_apps
from os import system


class ShellWin(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()
        self.setParent(parent)

        # Create Bash section
        self.installed_apps = get_installed_apps()
        self.appBash = ShellBox("Bash (Default)",
                                "bash",
                                "Assets/Apps/Shells/bash.png",
                                "Unix shell and command language written for the GNU Project as a replacement for the Bourne shell. <font color='red'>Do not remove this package!</font>",
                                self,
                                self.parent().parent().barBottom,
                                True
                                )

        # Create Shell section
        self.appSh = ShellBox("Sh",
                              "sh",
                              "Assets/Apps/Shells/sh.png",
                              "Shell command-line interpreter for computer operating systems. <font color='red'>Do not remove this package!</font>",
                              self,
                              self.parent().parent().barBottom,
                              True
                              )

        # Create ZSH section
        self.appZsh = ShellBox("Zsh",
                               "zsh",
                               "Assets/Apps/Shells/zsh.png",
                               "Extended Bourne Shell that offers numerous improvements, including features borrowed from Bash, ksh, and tcsh.",
                               self,
                               self.parent().parent().barBottom
                               )

        # Create fish section
        self.appFish = ShellBox("Fish",
                                "fish",
                                "Assets/Apps/Shells/fish.png",
                                "Friendly interactive shell. Smart and user-friendly command line shell.",
                                self,
                                self.parent().parent().barBottom
                                )

        # Create Oh-My-Zsh section
        self.extOhMyZsh = \
            ButtonBox(
                "Oh-My-Zsh",
                "Assets/Apps/Shells/ohmyzsh.png",
                "<font color=\"orange\">Requires zsh.</font> A delightful, open-source, community-driven framework for managing your Zsh configuration. It provides a wealth of helpful functions, plugins, themes, and other features that make you shout with joy.", []
            )
        # Add Oh-My-Zsh Theme Buttons
        self.layOhMyZsh = QGridLayout()
        self.layOhMyZsh.addWidget(CommandButton(
            QIcon("Assets/configure.png"), "Use Elagoht Theme",
            self.zsh_theme_setter("elagoht"), self))
        self.layOhMyZsh.addWidget(CommandButton(
            QIcon("Assets/configure.png"), "Use Elagoht Iconless Theme",
            self.zsh_theme_setter("elagoht-safe"), self), 0, 1)
        self.layOhMyZsh.addWidget(CommandButton(
            QIcon("Assets/configure.png"), "Use BashPlus Theme",
            self.zsh_theme_setter("bashplus"), self))
        self.layOhMyZsh.addWidget(CommandButton(
            QIcon("Assets/configure.png"), "Use Robby Russell Theme",
            self.zsh_theme_setter("robbyrussell"), self))
        self.extOhMyZsh.glyApp.addLayout(self.layOhMyZsh)
        # Create Oh-My-Zsh install/uninstall buttons
        self.btnOhMyZshInstall = CommandButton(
            QIcon("Assets/install.png"), "Install",
            long_bash_script("LBSF/OhMyZsh.sh"),
            self.extOhMyZsh, (self.check_oh_my_zsh,), True)
        self.btnOhMyZshUninstall = CommandButton(
            QIcon("Assets/uninstall.png"), "Uninstall",
            """pkexec rm -rf /root/.oh-my-zsh/
                rm -rf $HOME/.oh-my-zsh/
                pkexec rm /root/.zshrc
                rm $HOME/.zshrc
            """,
            self.extOhMyZsh, (self.check_oh_my_zsh,), True, True)

        # Create SyntShell section
        # ! Looks like it's not working. Will be added when it's ready.

        # Insert groupboxes to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.appBash)
        self.layout.addWidget(self.appSh, 0, 1)
        self.layout.addWidget(self.appZsh)
        self.layout.addWidget(self.appFish)
        self.layout.addWidget(self.extOhMyZsh, 2, 0, 1, 2)
        self.layout.setRowStretch(3, 1)

        # Initialize
        self.check_oh_my_zsh()

    # Shortcut for OhMyZsh theme setter.
    def zsh_theme_setter(self, theme: str) -> str:
        return fr"""[ \"$(grep \"^ZSH_THEME=\" $HOME/.zshrc)\" ] && sudo -i sed -i "s/^ZSH_THEME=.*/ZSH_THEME=\"{theme}\"/" $HOME/.zshrc
                   sudo [ \"$(sudo grep \"^ZSH_THEME=\" /root/.zshrc)\" ] && sudo -i sed -i "s/^ZSH_THEME=.*/ZSH_THEME=\"{theme}\"/" /root/.zshrc"""

    # Show/hide OhMyZsh Install button
    def check_oh_my_zsh(self) -> None:
        installed = system("[ -d ~/.oh-my-zsh ]") == 0
        to_show = self.btnOhMyZshUninstall if installed else self.btnOhMyZshInstall
        to_hide = self.btnOhMyZshInstall if installed else self.btnOhMyZshUninstall
        self.extOhMyZsh.layButtons.addWidget(to_show)
        self.extOhMyZsh.layButtons.removeWidget(to_hide)
        to_show.show()
        to_hide.hide()
