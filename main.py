from app.views.interfaces.ui_home import Home
import sys
from app import app

if __name__ == "__main__":
    window = Home()
    sys.exit(app.exec())
