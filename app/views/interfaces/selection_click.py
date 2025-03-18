from qt_core import *

class SelectionClick(QMainWindow):
    def __init__(self, screen_geometry, all_windows, x, y):
        super().__init__()

        self.setWindowTitle("Tela Completa")

        self.px = x
        self.py = y

        self.all_windows = all_windows

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.setGeometry(screen_geometry)

        self.setWindowState(Qt.WindowFullScreen)

        self.setWindowOpacity(0.01)

        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            position = event.position()
            x = int(position.x())
            y = int(position.y())

            

            for window in self.all_windows:
                window.close()
