from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLabel
from enum import Enum

# Definindo o Enum Layout
class Layout(Enum):
    VERTICAL = "V"
    HORIZONTAL = "H"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo com QComboBox e Enum")

        # Widget Central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)

        # ComboBox (Menu de Seleção)
        self.session2_top_type_trigger = QComboBox()
        self.session2_top_type_trigger.currentIndexChanged.connect(self.on_trigger_type_changed)

        # Adiciona valores do Enum no ComboBox
        for value in Layout.__members__.values():
            self.session2_top_type_trigger.addItem(value.value, value)  # Nome como texto visível, Enum como userData

        # Adicionando ao Layout
        layout.addWidget(self.session2_top_type_trigger)

    def on_trigger_type_changed(self, index):
        # Obtém o texto visível e o userData do item selecionado
        value = self.session2_top_type_trigger.itemData(index)
        print(f"Valor associado ao item selecionado: {value}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
