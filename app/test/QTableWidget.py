from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QHeaderView

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Criando a tabela
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(0)  # Iniciar sem nenhuma linha
        self.table_widget.setColumnCount(3)  # Definir 3 colunas
        self.table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table_widget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table_widget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)

        # Adicionar botão para inserir linha
        self.add_button = QPushButton("Adicionar Linha", self)
        self.add_button.clicked.connect(self.add_row)

        layout = QVBoxLayout(self)
        layout.addWidget(self.table_widget)
        layout.addWidget(self.add_button)

    def add_row(self):
        row_position = self.table_widget.rowCount()  # Pega a posição da próxima linha
        self.table_widget.insertRow(row_position)  # Insere a nova linha

        # Adicionando dados nas células da nova linha
        self.table_widget.setItem(row_position, 0, QTableWidgetItem("Item 1"))
        self.table_widget.setItem(row_position, 1, QTableWidgetItem("Item 2"))
        self.table_widget.setItem(row_position, 2, QTableWidgetItem("Item 3"))

app = QApplication([])
window = MyWidget()
window.show()
app.exec()
