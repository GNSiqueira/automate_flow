from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QAbstractItemView

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Criando a tabela
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(3)

        # Preencher a tabela com dados de exemplo
        for row in range(5):
            for col in range(3):
                self.table_widget.setItem(row, col, QTableWidgetItem(f"Item {row+1},{col+1}"))

        # Desabilitar qualquer tipo de seleção
        self.table_widget.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        layout = QVBoxLayout(self)
        layout.addWidget(self.table_widget)

app = QApplication([])
window = MyWidget()
window.show()
app.exec()
