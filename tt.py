import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtGui import QColor, QPalette

class TableExample(QWidget):
    def __init__(self):
        super().__init__()

        # Definindo a palete para o fundo azul claro
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(173, 216, 230))  # Azul claro
        self.setPalette(palette)

        # Configurando a tabela
        self.setWindowTitle("Exemplo de Tabela")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.table_widget = QTableWidget()

        # Definindo o número de linhas e colunas
        self.table_widget.setRowCount(8)
        self.table_widget.setColumnCount(4)

        # Definindo os cabeçalhos das colunas
        self.table_widget.setHorizontalHeaderLabels(["Full Name", "Age", "Job Title", "Location"])

        # Adicionando dados
        data = [
            ("Vincent Williamson", 31, "iOS Developer", "Washington"),
            ("Joseph Smith", 27, "Project Manager", "Somerville, MA"),
            ("Justin Block", 26, "Front-End Developer", "Los Angeles"),
            ("Sean Quamon", 26, "Web Designer", "San Francisco"),
            ("Keith Carter", 20, "Graphic Designer", "New York, NY"),
            ("Austin Medina", 32, "Photographer", "New York"),
            ("Vincent Williamson", 31, "iOS Developer", "Washington"),
            ("Joseph Smith", 27, "Project Manager", "Somerville, MA"),
        ]

        for row, (name, age, job, location) in enumerate(data):
            self.table_widget.setItem(row, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(age)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(job))
            self.table_widget.setItem(row, 3, QTableWidgetItem(location))

        # Estilizando a tabela
        self.table_widget.setStyleSheet("""
            QTableWidget {
                border: none;
                font-size: 14px;
                gridline-color: #d3d3d3;
            }
            QHeaderView::section {
                background-color: #ffffff;  /* Cores de fundo dos cabeçalhos */
                padding: 4px;
                font-weight: bold;
            }
            QTableWidgetItem {
                padding: 8px;
            }
        """)

        layout.addWidget(self.table_widget)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    table_example = TableExample()
    table_example.show()
    sys.exit(app.exec())
