#!/bin/env bash
echo -e "\033[1;32m==>\033[0m Installing OhMyZsh for $USER and root users."
sleep 1
curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | bash
curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | sudo -i bash
echo -e "\033[1;32m==>\033[0m Installing Elagoht Theme"
curl -sfSL "https://raw.githubusercontent.com/Elagoht/BashPlusZshTheme/main/bashplus.zsh-theme" -o ~/.oh-my-zsh/themes/bashplus.zsh-theme
sudo curl -sfSL "https://raw.githubusercontent.com/Elagoht/BashPlusZshTheme/main/bashplus.zsh-theme" -o /root/.oh-my-zsh/themes/bashplus.zsh-theme
sleep 1
echo -e "\033[1;32m==>\033[0m Installing Elagoht-Safe Theme"
curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht.zsh-theme" -o ~/.oh-my-zsh/themes/elagoht.zsh-theme
sudo curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht.zsh-theme" -o /root/.oh-my-zsh/themes/elagoht.zsh-theme
sleep 1
echo -e "\033[1;32m==>\033[0m Installing Bash Plus Theme"
curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht-safe.zsh-theme" -o ~/.oh-my-zsh/themes/elagoht-safe.zsh-theme
sudo curl -sfSL "https://raw.githubusercontent.com/Elagoht/Elagoht.zsh-theme/main/elagoht-safe.zsh-theme" -o /root/.oh-my-zsh/themes/elagoht-safe.zsh-theme
sleep 1
echo -e "\033[1;32m==>\033[0m Installing Syntax Highlighting Plugin"
git clone https://github.com/zsh-users/zsh-syntax-highlighting "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
sudo -i git clone https://github.com/zsh-users/zsh-syntax-highlighting "${ZSH_CUSTOM:-/root/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
sleep 1
echo -e "\033[1;32m==>\033[0m Installing Auto Suggestions Plugin"
git clone https://github.com/zsh-users/zsh-autosuggestions "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
sudo -i git clone https://github.com/zsh-users/zsh-autosuggestions "${ZSH_CUSTOM:-/root/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
echo -e "\033[1;32m==>\033[0m Enabling Plugins"
sleep 1
sed -i "s/plugins=.*/plugins=(git virtualenv zsh-autosuggestions zsh-syntax-highlighting)/" ~/.zshrc
sudo sed -i "s/plugins=.*/plugins=(git virtualenv zsh-autosuggestions zsh-syntax-highlighting)/" /root/.zshrc
echo -e "\033[1;32m==>\033[0m Installation done!"
sleep 1
