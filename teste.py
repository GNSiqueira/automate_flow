import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QGuiApplication

class ClickWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Defina o título da janela
        self.setWindowTitle("Capturar Clique e Tela")
        self.setGeometry(100, 100, 400, 400)  # Posição e tamanho da janela

        # Adiciona um QLabel para mostrar as coordenadas
        self.label = QLabel("Clique na janela", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(100, 180, 200, 40)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        # Captura as coordenadas do clique
        x = event.x()
        y = event.y()

        # Obtém a posição do clique no monitor
        screen_number = self.get_screen_number(x, y)

        # Exibe as coordenadas e o número da tela
        self.label.setText(f"Clicou em: ({x}, {y})\nNa tela: {screen_number + 1}")

    def get_screen_number(self, x, y):
        # Obtém a posição global do clique
        global_pos = self.mapToGlobal(QPoint(x, y))

        # Obtém todos os monitores conectados
        screens = QGuiApplication.screens()

        for i, screen in enumerate(screens):
            screen_rect = screen.geometry()
            if screen_rect.contains(global_pos):  # Verifica se a posição do clique está dentro da área do monitor
                return i
        return -1  # Caso não encontre a tela

# Cria o aplicativo PySide6
app = QApplication(sys.argv)

# Cria a janela
window = ClickWindow()
window.show()

# Executa o loop de eventos
sys.exit(app.exec())
