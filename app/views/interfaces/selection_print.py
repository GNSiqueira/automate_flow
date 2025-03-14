from qt_core import *
from PIL import ImageGrab
from time import sleep
from app.utils.util import repositories, os

class SelectionPrint(QMainWindow):
    def __init__(self, screen_geometry, fun):
        super().__init__()
        if not callable(fun):
            raise TypeError(f"fun deve ser uma função, mas foi passado: {type(fun).__name__}")
        self.fun = fun

        self.setWindowTitle("Tela Completa")

        self.windows_screen = None

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.setGeometry(screen_geometry)

        self.setWindowState(Qt.WindowFullScreen)

        self.setWindowOpacity(0.5)

        self.start_point = None
        self.end_point = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_point = event.pos()
            self.update()
            self.capture_screen()
            self.clear_lines()

    def paintEvent(self, event):
        if self.start_point is not None and self.end_point is not None:
            painter = QPainter(self)
            pen = QPen(Qt.red, 2)
            painter.setPen(pen)

            rect = QRect(self.start_point, self.end_point)
            painter.drawRect(rect)

    def set_windows(self, data):
        self.windows_screen = data
    
    def close_windows(self):
        for window in self.windows_screen:
            window.close()
    
    def clear_lines(self):
        self.start_point = None
        self.end_point = None
        self.repaint()

    def capture_screen(self):
        if self.start_point is not None and self.end_point is not None:
            self.setWindowOpacity(0)
            self.hide()

            sleep(0.2)

            x1 = self.geometry().x() + self.start_point.x()
            y1 = self.geometry().y() + self.start_point.y()
            x2 = self.geometry().x() + self.end_point.x()
            y2 = self.geometry().y() + self.end_point.y()

            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)

            bbox = (x1, y1, x2, y2)
            screenshot = ImageGrab.grab(bbox)
            
            repository, repository_image = repositories()

            count = 0
            while os.path.exists(f"{repository_image}/screenshot{count}.png"):
                count += 1

            screenshot.save(f"{repository_image}/screenshot{count}.png")
            print(f"Captura de tela salva como 'screenshot{count}.png'")

            self.close_windows()
            self.fun(f'screenshot{count}.png')
            