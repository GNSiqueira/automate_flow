from qt_core import QApplication
from app.views.interfaces.ui_home import Home
import sys, os
from app import app

# Adiciona o diretório base ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class Window(Home):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    window = Window()
    window.show()
    sys.exit(app.exec())
