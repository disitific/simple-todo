pkgname=simple-todo
pkgver=1.0
pkgrel=1
pkgdesc="A minimalist PyQt6 ToDo application"
arch=('any')
license=('GPL')
depends=('python' 'python-pyqt6')
source=('main.py' 'simple-todo.desktop')
sha256sums=('SKIP' 'SKIP')

package() {
    # 1. Install the Python script into /usr/bin/ and make it executable
    install -Dm755 "$srcdir/main.py" "$pkgdir/usr/bin/simple-todo"

    # 2. Install the desktop entry file so the launcher sees it
    install -Dm644 "$srcdir/simple-todo.desktop" "$pkgdir/usr/share/applications/simple-todo.desktop"
}