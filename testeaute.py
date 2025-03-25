import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Signal

class main(QWidget):
    # Sinal que será emitido ao fechar a janela
    sinal_atualizar = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Segunda Janela")
        self.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout()

        

        
# Inicializa o aplicativo
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main()
    janela.show()
    sys.exit(app.exec())
