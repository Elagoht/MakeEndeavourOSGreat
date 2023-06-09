#!/bin/env bash
echo -e "\033[1;32m==>\033[0m Installing OhMyZsh for $USER and root users."
# Install OhMyZsh
curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | bash
curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | sudo -i bash
# Install Elagoht Theme
echo -e "\033[1;32m==>\033[0m Installing Elagoht Theme"
curl -sfSL "https://raw.githubusercontent.com/Elagoht/BashPlusZshTheme/main/bashplus.zsh-theme" -o ~/.oh-my-zsh/themes/bashplus.zsh-theme
sudo curl -sfSL "https://raw.githubusercontent.com/Elagoht/BashPlusZshTheme/main/bashplus.zsh-theme" -o /root/.oh-my-zsh/themes/bashplus.zsh-theme
# Install Elagoht Safe Theme
echo -e "\033[1;32m==>\033[0m Installing Elagoht-Safe Theme"
curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht.zsh-theme" -o ~/.oh-my-zsh/themes/elagoht.zsh-theme
sudo curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht.zsh-theme" -o /root/.oh-my-zsh/themes/elagoht.zsh-theme
# Install Bash Plus Theme
echo -e "\033[1;32m==>\033[0m Installing Bash Plus Theme"
curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht-safe.zsh-theme" -o ~/.oh-my-zsh/themes/elagoht-safe.zsh-theme
sudo curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht-safe.zsh-theme" -o /root/.oh-my-zsh/themes/elagoht-safe.zsh-theme
# Install Syntax Highlighting
echo -e "\033[1;32m==>\033[0m Installing Syntax Highlighting Plugin"
git clone https://github.com/zsh-users/zsh-syntax-highlighting ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
sudo -i git clone https://github.com/zsh-users/zsh-syntax-highlighting /root/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
# Install Auto Suggestions
echo -e "\033[1;32m==>\033[0m Installing Auto Suggestions Plugin"
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
sudo -i git clone https://github.com/zsh-users/zsh-autosuggestions /root/.oh-my-zsh/custom/plugins/zsh-autosuggestions
# Enable Plugins
echo -e "\033[1;32m==>\033[0m Enabling Plugins"
sed -i "s/plugins=.*/plugins=(git virtualenv zsh-autosuggestions zsh-syntax-highlighting)/" ~/.zshrc
sudo sed -i "s/plugins=.*/plugins=(git virtualenv zsh-autosuggestions zsh-syntax-highlighting)/" /root/.zshrc
echo -e "\033[1;32m==>\033[0m Installation done!"
