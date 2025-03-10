from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu de Seleção com QListWidget")

        # Widget Central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)

        # Lista de Seleção
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Item 1", "Item 2", "Item 3"])  # Adiciona itens

        # Rótulo para exibir a seleção
        self.label = QLabel("Selecione um item da lista")

        # Conectando a seleção de item
        self.list_widget.currentItemChanged.connect(self.update_label)

        # Adicionando ao Layout
        layout.addWidget(self.list_widget)
        layout.addWidget(self.label)

    def update_label(self, item):
        if item:
            self.label.setText(f"Você selecionou: {item.text()}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
