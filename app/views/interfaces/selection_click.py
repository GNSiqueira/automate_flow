from qt_core import *

class SelectionClick(QMainWindow):
    def __init__(self, screen_geometry, all_windows, x, y, fun):
        super().__init__()

        if not callable(fun):
            raise TypeError(f"fun deve ser uma função, mas foi passado: {type(fun).__name__}")
        self.fun = fun

        self.setWindowTitle("Tela Completa")

        self.px = x
        self.py = y

        self.all_windows = all_windows

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.setGeometry(screen_geometry)

        self.setWindowState(Qt.WindowFullScreen)

        self.setWindowOpacity(0.3)

        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            position = event.position()
            x = int(position.x() + self.px)
            y = int(position.y() + self.py)

            for window in self.all_windows:
                window.close()
            texto = (f"x={x}, y={y}")
            self.fun(texto, x, y)



