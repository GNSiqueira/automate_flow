from app.views.interfaces.new_configs import NewConfigs
import sys
from app import app

if __name__ == "__main__":
    window = NewConfigs()
    sys.exit(app.exec())
