from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtGui import QIcon
from Utilities import ShellBox, ButtonBox, CommandButton


class ShellWin(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create Bash section
        self.appBash = ShellBox("Bash (Default)",
                                "bash",
                                "GUI/Assets/Apps/Shells/bash.png",
                                "Unix shell and command language written for the GNU Project as a replacement for the Bourne shell. <font color='red'>Do not remove this package!</font>",
                                True
                                )

        # Create Shell section
        self.appSh = ShellBox("Sh",
                              "sh",
                              "GUI/Assets/Apps/Shells/sh.png",
                              "Shell command-line interpreter for computer operating systems. <font color='red'>Do not remove this package!</font>",
                              True
                              )

        # Create ZSH section
        self.appZsh = ShellBox("Zsh",
                               "zsh",
                               "GUI/Assets/Apps/Shells/zsh.png",
                               "extended Bourne shell with many improvements, including some features of Bash, ksh, and tcsh."
                               )

        # Create fish section
        self.appFish = ShellBox("Fish",
                                "fish",
                                "GUI/Assets/Apps/Shells/fish.png",
                                "Friendly interactive shell. Smart and user-friendly command line shell"
                                )

        # Create Oh-My-Zsh section
        self.extOhMyZsh = \
            ButtonBox(
                "Oh-My-Zsh",
                "GUI/Assets/Apps/Shells/ohmyzsh.png",
                "<font color=\"orange\">Requires zsh.</font> Delightful, open source, community-driven framework for managing your Zsh configuration. It comes bundled with thousands of helpful functions, helpers, plugins, themes, and a few things that make you shout...", (
                    CommandButton(QIcon("GUI/Assets/install.png"), "Install",
                                  r"""curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | bash;
                                  curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | sudo -i bash;
                                  echo Installing Elagoht Theme
                                  curl -sfSL "https://raw.githubusercontent.com/Elagoht/BashPlusZshTheme/main/bashplus.zsh-theme" -o ~/.oh-my-zsh/themes/bashplus.zsh-theme;
                                  sudo curl -sfSL "https://raw.githubusercontent.com/Elagoht/BashPlusZshTheme/main/bashplus.zsh-theme" -o /root/.oh-my-zsh/themes/bashplus.zsh-theme;
                                  sleep 1
                                  echo Installing Elagoht-Safe Theme
                                  curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht.zsh-theme" -o ~/.oh-my-zsh/themes/elagoht.zsh-theme;
                                  sudo curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht.zsh-theme" -o /root/.oh-my-zsh/themes/elagoht.zsh-theme
                                  sleep 1
                                  echo Installing Bash Plus Theme
                                  curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht-safe.zsh-theme" -o ~/.oh-my-zsh/themes/elagoht-safe.zsh-theme;
                                  sudo curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht-safe.zsh-theme" -o /root/.oh-my-zsh/themes/elagoht-safe.zsh-theme
                                  sleep 1
                                  echo Installing Syntax Highlighting Plugin
                                  git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
                                  sudo -i git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-/root/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
                                  sleep 1
                                  echo Installing Auto Suggestions Plugin
                                  git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
                                  sudo -i git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-/root/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
                                  echo Enabling Plugins
                                  sleep 1
                                  sed -i "s/plugins=.*/plugins=(git virtualenv zsh-autosuggestions zsh-syntax-highlighting)/" ~/.zshrc
                                  sudo sed -i "s/plugins=.*/plugins=(git virtualenv zsh-autosuggestions zsh-syntax-highlighting)/" /root/.zshrc
                                  """,
                                  self),
                    CommandButton(QIcon("GUI/Assets/uninstall.png"), "Uninstall",
                                  r"""echo Confirm that you really want to uninstall oh-my-zsh; rm -ri $HOME/.oh-my-zsh/;
                                  sudo -i rm -ri $HOME/.oh-my-zsh/""",
                                  self)
                )
            )
        self.layOhMyZsh = QGridLayout(self.extOhMyZsh)
        self.layOhMyZsh.addWidget(
            CommandButton(QIcon("GUI/Assets/configure.png"), "Use Elagoht Theme",
                          self.zsh_theme_setter("elagoht"), self))
        self.layOhMyZsh.addWidget(
            CommandButton(QIcon("GUI/Assets/configure.png"), "Use Elagoht Iconless Theme",
                          self.zsh_theme_setter("elagoht-safe"), self),
            0, 1)
        self.layOhMyZsh.addWidget(
            CommandButton(QIcon("GUI/Assets/configure.png"), "Use BashPlus Theme",
                          self.zsh_theme_setter("bashplus"), self))
        self.layOhMyZsh.addWidget(
            CommandButton(QIcon("GUI/Assets/configure.png"), "Use Robby Russell Theme",
                          self.zsh_theme_setter("robbyrussell"), self))
        self.extOhMyZsh.glyApp.addLayout(self.layOhMyZsh)

        # Create SyntShell section
        # ! Looks like it's not working. Will be added when it's ready.

        # Insert groupboxes to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.appBash)
        self.layout.addWidget(self.appSh, 0, 1)
        self.layout.addWidget(self.appZsh)
        self.layout.addWidget(self.appFish)
        self.layout.addWidget(self.extOhMyZsh)

    def zsh_theme_setter(self, theme: str):
        return fr"""[ \"$(grep \"^ZSH_THEME=\" $HOME/.zshrc)\" ] && sudo -i sed -i "s/^ZSH_THEME=.*/ZSH_THEME=\"{theme}\"/" $HOME/.zshrc
                   sudo [ \"$(sudo grep \"^ZSH_THEME=\" /root/.zshrc)\" ] && sudo -i sed -i "s/^ZSH_THEME=.*/ZSH_THEME=\"{theme}\"/" /root/.zshrc"""
