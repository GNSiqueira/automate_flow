import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Signal

class SegundaJanela(QWidget):
    # Sinal que será emitido ao fechar a janela
    sinal_atualizar = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Segunda Janela")
        self.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout()

        self.label_info = QLabel("Atualizando arquivo...", self)
        layout.addWidget(self.label_info)

        self.btn_fechar = QPushButton("Fechar e Atualizar", self)
        self.btn_fechar.clicked.connect(self.fechar_e_atualizar)
        layout.addWidget(self.btn_fechar)

        self.setLayout(layout)

    def fechar_e_atualizar(self):
        """Simula uma atualização do arquivo e emite o sinal."""
        with open("dados.txt", "w") as arquivo:
            arquivo.write("Novo conteúdo atualizado!\n")

        self.sinal_atualizar.emit()  # Emite o sinal para a janela principal
        self.close()  # Fecha a janela


class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label_status = QLabel("Arquivo não atualizado.", self)
        self.layout.addWidget(self.label_status)

        self.btn_abrir_janela = QPushButton("Abrir Segunda Janela", self)
        self.btn_abrir_janela.clicked.connect(self.abrir_segunda_janela)
        self.layout.addWidget(self.btn_abrir_janela)

        self.setLayout(self.layout)

    def abrir_segunda_janela(self):
        """Abre a segunda janela e conecta o sinal de atualização."""
        self.segunda_janela = SegundaJanela()
        self.segunda_janela.sinal_atualizar.connect(self.atualizar_info)
        self.segunda_janela.show()

    def atualizar_info(self):
        """Lê o arquivo e atualiza a interface após fechar a segunda janela."""
        try:
            with open("dados.txt", "r") as arquivo:
                conteudo = arquivo.read().strip()
                self.label_status.setText(f"Conteúdo atualizado: {conteudo}")
        except FileNotFoundError:
            self.label_status.setText("Erro ao carregar arquivo!")

# Inicializa o aplicativo
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())
