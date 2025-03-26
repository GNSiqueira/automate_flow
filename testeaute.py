import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup, QPushButton, QLabel, QWidget

class MultiRadioButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo com Múltiplos RadioButtons")

        self.layout = QVBoxLayout()

        # Grupo 1: Cores
        self.label_grupo1 = QLabel("Selecione uma cor:")
        self.layout.addWidget(self.label_grupo1)
        self.grupo1_layout = QHBoxLayout()

        self.radio_vermelho = QRadioButton("Vermelho")
        self.radio_azul = QRadioButton("Azul")
        self.radio_verde = QRadioButton("Verde")

        self.grupo1_layout.addWidget(self.radio_vermelho)
        self.grupo1_layout.addWidget(self.radio_azul)
        self.grupo1_layout.addWidget(self.radio_verde)
        self.layout.addLayout(self.grupo1_layout)

        self.grupo1 = QButtonGroup()  # Grupo separado para as cores
        self.grupo1.addButton(self.radio_vermelho)
        self.grupo1.addButton(self.radio_azul)
        self.grupo1.addButton(self.radio_verde)

        # Grupo 2: Animais
        self.label_grupo2 = QLabel("Selecione um animal:")
        self.layout.addWidget(self.label_grupo2)
        self.grupo2_layout = QHBoxLayout()

        self.radio_cachorro = QRadioButton("Cachorro")
        self.radio_gato = QRadioButton("Gato")
        self.radio_passaro = QRadioButton("Pássaro")

        self.grupo2_layout.addWidget(self.radio_cachorro)
        self.grupo2_layout.addWidget(self.radio_gato)
        self.grupo2_layout.addWidget(self.radio_passaro)
        self.layout.addLayout(self.grupo2_layout)

        self.grupo2 = QButtonGroup()  # Grupo separado para os animais
        self.grupo2.addButton(self.radio_cachorro)
        self.grupo2.addButton(self.radio_gato)
        self.grupo2.addButton(self.radio_passaro)

        # Botão para verificar seleções
        self.botao = QPushButton("Confirmar Seleções")
        self.botao.clicked.connect(self.verificar_selecoes)
        self.layout.addWidget(self.botao)

        # Label para mostrar os resultados
        self.resultado_label = QLabel("")
        self.layout.addWidget(self.resultado_label)

        self.setLayout(self.layout)

    def verificar_selecoes(self):
        # Verifica seleção do grupo 1
        selecao_grupo1 = ""
        if self.radio_vermelho.isChecked():
            selecao_grupo1 = "Vermelho"
        elif self.radio_azul.isChecked():
            selecao_grupo1 = "Azul"
        elif self.radio_verde.isChecked():
            selecao_grupo1 = "Verde"

        # Verifica seleção do grupo 2
        selecao_grupo2 = ""
        if self.radio_cachorro.isChecked():
            selecao_grupo2 = "Cachorro"
        elif self.radio_gato.isChecked():
            selecao_grupo2 = "Gato"
        elif self.radio_passaro.isChecked():
            selecao_grupo2 = "Pássaro"

        # Mostra as seleções
        self.resultado_label.setText(f"Cor selecionada: {selecao_grupo1}\nAnimal selecionado: {selecao_grupo2}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MultiRadioButtonApp()
    janela.show()
    sys.exit(app.exec())
