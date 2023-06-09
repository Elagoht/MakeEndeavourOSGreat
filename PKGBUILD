# Maintainer: Furkan Baytekin (Elagoht) <furkanbaytekin@gmail.com>
pkgname=make-endeavouros-great-git
pkgver=0.1
pkgrel=1
pkgdesc="Make Endeavour Os Great"
arch=("any")
url="https://github.com/Elagoht/MakeEndeavourOSGreat"
license=('GPL')
depends=("base-devel" "git" "python-pyqt5" "kvantum")
optdepends=("kvantum-theme-libadwaita")
provides=(make-endeavouros-great)
source=("git+https://github.com/Elagoht/MakeEndeavourOSGreat")
md5sums=("SKIP")

prepare() {
    cat > $srcdir/MakeEndeavourOSGreat.desktop << EOF
[Desktop Entry]
Name=EOS Tweaker
GenericName=Tweaker Tool
Description=Make Endeavour OS Great
Icon=/usr/share/MakeEndeavourOSGreat/icon.png
Path=/usr/share/MakeEndeavourOSGreat
Exec=make-endeavouros-great
Type=Application
Categories=Utility;
Keywords=tweaks;tweaker;settings;configure
EOF
    cat > $srcdir/make-endeavouros-great << EOF
/usr/share/MakeEndeavourOSGreat/main.py
EOF
}

package() {
	install -d $pkgdir/usr/share/MakeEndeavourOSGreat
    mv $srcdir/MakeEndeavourOSGreat/GUI/* $pkgdir/usr/share/MakeEndeavourOSGreat
    install -d $pkgdir/usr/share/applications
    install -D $srcdir/MakeEndeavourOSGreat.desktop -t $pkgdir/usr/share/applications/
    install -d $pkgdir/usr/bin
    install -D $srcdir/make-endeavouros-great -t $pkgdir/usr/bin
}

