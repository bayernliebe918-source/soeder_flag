# Maintainer: Dein Name <dein.email@example.com>
pkgname=soeder-flag
pkgver=1.0
pkgrel=1
pkgdesc="Terminal-Bayernflaggen-Animation für König Söder"
arch=('any')
url="https://github.com/bayernliebe918-source/soeder-flag"
license=('MIT')

depends=('python' 'python-colorama' 'python-pyfiglet')

source=("soeder_flag.py")
sha256sums=('SKIP')  # nur für kleine lokale Scripts okay

package() {
    # Skript ins Standard-Bin-Verzeichnis kopieren
    install -Dm755 soeder_flag.py "$pkgdir/usr/bin/soeder-flag"
}
