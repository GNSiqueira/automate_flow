from PySide6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget, QFileDialog, QMenu
from PySide6.QtCore import QEvent, Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selecionar Arquivo ou Pasta")
        self.setGeometry(200, 200, 400, 100)

        self.input_path = QLineEdit("Clique para selecionar um arquivo ou pasta...")
        self.input_path.setReadOnly(True)  # Evita edição manual
        self.input_path.installEventFilter(self)  # Adiciona filtro de eventos

        layout = QVBoxLayout()
        layout.addWidget(self.input_path)
        self.setLayout(layout)

    def eventFilter(self, obj, event):
        if obj == self.input_path and event.type() == QEvent.MouseButtonPress:
            self.showSelectionMenu()
            return True  # Bloqueia o evento original para evitar edição manual

        return super().eventFilter(obj, event)

    def showSelectionMenu(self):
        menu = QMenu(self)

        action_file = menu.addAction("Selecionar Arquivo")
        action_folder = menu.addAction("Selecionar Pasta")

        action = menu.exec(self.mapToGlobal(self.input_path.pos() + self.input_path.rect().bottomLeft()))

        if action == action_file:
            self.selectFile()
        elif action == action_folder:
            self.selectFolder()

    def selectFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione um arquivo")
        if file_path:
            self.input_path.setText(file_path)

    def selectFolder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Selecione uma pasta")
        if folder_path:
            self.input_path.setText(folder_path)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
