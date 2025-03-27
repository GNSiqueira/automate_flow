import sys
from PySide6.QtWidgets import (QApplication, QWidget, QTableWidget,
                                QTableWidgetItem, QVBoxLayout, QHeaderView,
                                QAbstractItemView)
from PySide6.QtGui import QColor, QFont, QPalette
from PySide6.QtCore import Qt

class ElegantTableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employee Directory")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #f4f6f9;")

        # Create main layout
        layout = QVBoxLayout()

        # Create table
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.setLayout(layout)

        # Prepare data
        data = [
            ["Vincent Williamson", 31, "iOS Developer", "Washington"],
            ["Joseph Smith", 27, "Project Manager", "Somerville, MA"],
            ["Justin Block", 28, "Front-end Developer", "Los Angeles"],
            ["Sean Guzman", 26, "Web Designer", "San Francisco"],
            ["Keith Carter", 30, "Graphic Designer", "New York, NY"],
            ["Austin Medina", 32, "Photographer", "New York"]
        ]

        # Set up table
        self.table.setColumnCount(4)
        self.table.setRowCount(len(data))
        self.table.setHorizontalHeaderLabels(["Full Name", "Age", "Job Title", "Location"])

        # Table global style
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border-radius: 10px;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #e0e0e0;
            }
        """)

        # Style table header
        header = self.table.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #3a7ca5;
                color: white;
                padding: 10px;
                border: none;
                font-weight: bold;
                font-size: 14px;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
        """)
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Populate table
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Make items read-only
                self.table.setItem(row, col, item)

        # Table interaction settings
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setAlternatingRowColors(True)
        self.table.setShowGrid(False)

        # Optional: Add some shadow effect
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f9;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
        """)

def main():
    app = QApplication(sys.argv)

    # Set application-wide font
    font = app.font()
    font.setFamily('Segoe UI')
    font.setPointSize(10)
    app.setFont(font)

    widget = ElegantTableWidget()
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
