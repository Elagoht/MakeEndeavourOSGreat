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
