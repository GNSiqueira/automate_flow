from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMenu

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selecionar Arquivo ou Pasta")
        self.setGeometry(200, 200, 400, 100)

        self.button = QPushButton("Selecionar Arquivo ou Pasta")
        self.button.setMenu(self.createMenu())  # Define o menu embutido

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def createMenu(self):
        """Cria o menu de seleção"""
        menu = QMenu(self)

        action_file = menu.addAction("Selecionar Arquivo")
        action_folder = menu.addAction("Selecionar Pasta")

        action_file.triggered.connect(self.selectFile)
        action_folder.triggered.connect(self.selectFolder)

        return menu

    def selectFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione um arquivo")
        if file_path:
            print(f"Arquivo selecionado: {file_path}")

    def selectFolder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Selecione uma pasta")
        if folder_path:
            print(f"Pasta selecionada: {folder_path}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
