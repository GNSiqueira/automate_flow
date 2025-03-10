import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QPen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marcação na Tela")
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 200, 20)

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
            self.start_point = None
            self.end_point = None

    def paintEvent(self, event):
        if self.start_point is not None and self.end_point is not None:
            painter = QPainter(self)
            pen = QPen(Qt.red, 2)
            painter.setPen(pen)

            rect = QRect(self.start_point, self.end_point)
            painter.drawRect(rect)
            self.label.setText(f"Posição do mouse: {self.end_point.x()}, {self.end_point.y()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
