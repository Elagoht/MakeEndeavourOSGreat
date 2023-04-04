# Commands to run to complete TODOs

---

Update the system:

```bash
sudo pacman -Sy
```

Upgrade the system:

```bash
sudo pacman -Su
```

---

Enable AUR on Pamac:

```bash
sudo sed -Ei '/EnableAUR/s/^#//' /etc/pamac.conf
```

Disable AUR on Pamac:

```bash
sudo sed -Ei '/EnableAUR/s/^/#/' /etc/pamac.conf
```

---

Install Pamac software manager:

```bash
sudo pacman -S pamac-aur
```

Remove Pamac software manager:

```bash
sudo pacman -R pamac-aur
```

---

Install paru:

```bash
sudo pacman -S paru
```

Remove yay:

```bash
sudo pacman -R yay
```

Install yay:

```bash
sudo pacman -S paru
```

Remove paru:

```bash
sudo pacman -R paru
```

---

Install gnome browser integration:

```bash
$aurhelper -S gnome-browser-connector
```

---

Detect AUR helper:

```bash
if [ -f /bin/paru ]; then
    aurhelper="/bin/paru"
elif [ -f /bin/yay ]; then 
    aurhelper="/bin/yay"
else
    aurhelper="/bin/pacman" # Change that piece.
fi
```

---

Install easy-effects:

```bash
sudo pacman -S easyeffects
```

---

Install `gnome-terminal`:

```bash
sudo pacman -S gnome-terminal
```

Remove `gnome-console`:

```bash
sudo pacman -R gnome-console
```

Install `gnome-console`:

```bash
sudo pacman -S gnome-console
```

Remove `gnome-terminal`:

```bash
sudo pacman -R gnome-terminal
```

---

Enable context menu icons:

```bash
gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "{'Gtk/ButtonImages': <1>, 'Gtk/MenuImages': <1>}"
```

---

Suggested Gnome extensions:

* <https://extensions.gnome.org/extension/1454/transparent-window/>
* <https://extensions.gnome.org/extension/3240/add-to-desktop/>
* <https://extensions.gnome.org/extension/1446/transparent-window-moving/>
* <https://extensions.gnome.org/extension/750/openweather/>
* <https://extensions.gnome.org/extension/2182/noannoyance/>
* <https://extensions.gnome.org/extension/770/force-quit/>
* <https://extensions.gnome.org/extension/307/dash-to-dock/>
* <https://extensions.gnome.org/extension/3740/compiz-alike-magic-lamp-effect/>
* <https://extensions.gnome.org/extension/3210/compiz-windows-effect/>
* <https://extensions.gnome.org/extension/615/appindicator-support/>
* <https://extensions.gnome.org/extension/3193/blur-my-shell/>
* <https://extensions.gnome.org/extension/517/caffeine/>
* <https://extensions.gnome.org/extension/3396/color-picker/>
* <https://extensions.gnome.org/extension/4257/scroll-panel/>
* <https://extensions.gnome.org/extension/355/status-area-horizontal-spacing/>

---

Installable nerd fonts:

* ttf-ubuntu-mono-nerd
* ttf-sourcecodepro-nerd
* ttf-roboto-mono-nerd
* ttf-jetbrains-mono-nerd
* ttf-firacode-nerd
* otf-droid-nerd
* ttf-dejavu-nerd
* ttf-hack-nerd

---

Developer Utilities:

* Common Utilities
  * code
  * visual-studio-code-bin
  * neovim
  * emacs
  * sqlitebrowser
  * mongodb-bin
  * mariadb
* HTML/CSS
  * bluefish
* Java
  * jdk-openjdk
  * jdk17-openjdk
  * jdk11-openjdk
  * jdk8-openjdk
* ttf-roboto-mono-nerd
* ttf-jetbrains-mono-nerd
* ttf-firacode-nerd
* otf-droid-nerd
* ttf-dejavu-nerd
* ttf-hack-nerd

---

Developer Utilities:

* Common Utilities
  * code
  * visual-studio-code-bin
  * neovim
  * emacs
  * sqlitebrowser
  * mongodb-bin
  * mariadb
* HTML/CSS
  * bluefish
* Java
  * jdk-openjdk
  * jdk17-openjdk
  * jdk11-openjdk
  * jdk8-openjdk
  * eclipse-java
* JavaScript
  * nodejs
  * npm
  * yarn
* Python
  * tk
  * bpython
  * idle
* C#
  * dotnet-sdk
* Rust
  * rustup
* R
  * r
  * rstudio-desktop-bin
* C/C++
  * codeblocks
  * linux-headers
  * linux-lts-headers
  * linux-zen-headers
  * clion
  * eclipse-cpp

---

Gnome shortcust:

```bash
gsettings set org.gnome.desktop.wm.keybindings panel-run-dialog "['<Super>r']"
gsettings set org.gnome.desktop.wm.keybindings show-desktop "['<Super>d']"
gsettings set org.gnome.desktop.wm.keybindings switch-applications "['<Super>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-applications-backward "['<Shift><Super>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-windows "['<Alt>Tab']"
gsettings set org.gnome.desktop.wm.keybindings toggle-fullscreen "['<Alt>F12']"
gsettings set org.gnome.desktop.wm.keybindings toggle-on-all-workspaces "['<Alt>F9']"
gsettings set org.gnome.shell.keybindings focus-active-notification "[]"
gsettings set org.gnome.shell.keybindings toggle-message-tray "['<Super>n']"
gsettings set org.gnome.settings-daemon.plugins.media-keys "['<Super><Shift>p']"
```

*Custom shortcuts:*

```bash
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name "Gnome Terminal"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding "<Control><Alt>t"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command "gnome-terminal"

gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ name "Gnome Terminal Alt"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ binding "<Super>Return"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ command "gnome-terminal"

gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/ name "Gnome System Monitor"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/ binding "<Control><Shift>Escape"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/ command "gnome-system-monitor"

gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom3/ name "Downloads"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom3/ binding "<Super>j"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom3/ command "xdg-open $HOME/Downloads"

gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings "['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom3/']"
```

---

Gaming applications:

* steam-runtime
* heroic-games-launcher
* itch
* mangohud
* goverlay-bin
* gamemode
* vkbasalt
* lutris
* protonge-custom-bin
* wine
* wine-gecko
* wine-mono
* winetricks
* bottles
* qjoypad
* jstest-gtk
* discord
* discover-overlay
* easyeffects
* teamspeak
