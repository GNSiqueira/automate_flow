from qt_core import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame
from app.utils.enums import Layout

class Ui(QMainWindow): 
    def __init__(self, alt=700, larg=500, FixedSize=False, layout: Layout = Layout.VERTICAL): 
        super().__init__()
        self.setWindowTitle("Automate Flow")
        if not self.objectName():
            self.setObjectName('Automate Flow')

        # Configurações da janela
        if FixedSize: 
            self.setFixedSize(larg, alt)
        else: 
            self.setGeometry(100, 100, larg, alt)

        # Configurações do layout principal
        self.__widget = QWidget(self)
        if layout == Layout.VERTICAL:
            self.layout = QVBoxLayout(self.__widget)
        elif layout == Layout.HORIZONTAL:
            self.layout = QHBoxLayout(self.__widget)
        else: 
            self.layout = QVBoxLayout(self.__widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Central Widget
        self.setCentralWidget(self.__widget)

    def setup(self, setup, expanding: int = None): 
        if isinstance(setup, (QFrame, QWidget)):
            if expanding:
                self.layout.addWidget(setup, expanding)
            else:
                self.layout.addWidget(setup)
        elif isinstance(setup, (QHBoxLayout, QVBoxLayout)):
            if expanding:
                self.layout.addLayout(setup, expanding)
            else:
                self.layout.addLayout(setup)
