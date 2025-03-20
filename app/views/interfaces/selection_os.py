from qt_core import *
from app.views.ui import Ui
from app.utils.enums import Layout
from app.utils.qt_layout import VLayout

class SelectionOs(Ui):
    def __init__(self, fun):
        super().__init__(alt=200, larg=250, FixedSize=True, layout=Layout.VERTICAL, modal=True)

        if callable(fun):
            self.fun = fun
        else:
            raise print("Erro: A função passada não é chamável!")

        self.container = VLayout(margin=10, spacing=10)

        command_os = [
            'Copiar',
            'Mover',
            'Deletar',
            'Criar',
            'Adicionar Comando'
        ]

        self.select_os = QComboBox(placeholderText='Selecione um comando os...')
        self.select_os.addItems(command_os)
        self.select_os.currentTextChanged.connect(self.selecionar_comando_os)

        self.one_input = None
        self.two_input = None
        self.button = None

        self.container.addWidget(self.select_os)

        self.setup(self.container)

        self.show()

    def selecionar_comando_os(self):
        texto = self.select_os.currentText()

        # Remove e exclui os widgets antigos
        if self.one_input:
            self.container.removeWidget(self.one_input)
            self.one_input.deleteLater()

        if self.two_input:
            self.container.removeWidget(self.two_input)
            self.two_input.deleteLater()

        if self.button:
            self.container.removeWidget(self.button)
            self.button.deleteLater()

        self.one_input = None
        self.two_input = None
        self.button = None

        # Criamos novos inputs conforme a seleção
        if texto in ['Copiar', 'Mover']:
            self.one_input = QLineEdit(placeholderText='Origem...')
            self.two_input = QLineEdit(placeholderText='Destino...')
        elif texto == 'Deletar':
            self.one_input = QLineEdit(placeholderText='Arquivo/Pasta a deletar...')
        elif texto == 'Criar':
            self.one_input = QLineEdit(placeholderText='Local de criação ...')
            self.two_input = QLineEdit(placeholderText='Nome da pasta...')
        elif texto == 'Adicionar Comando':
            self.one_input = QLineEdit(placeholderText='Novo comando...')


        # Adiciona eventos apenas para seleções que precisam de arquivo/pasta
        if self.one_input:
            self.one_input.installEventFilter(self)
            self.container.addWidget(self.one_input)
        if self.two_input:
            self.two_input.installEventFilter(self)
            self.container.addWidget(self.two_input)

        self.button = QPushButton('Salvar!')
        self.button.clicked.connect(self.salvar)

        self.container.addWidget(self.button)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if obj in [self.one_input, self.two_input]:
                if self.select_os.currentText() == 'Criar' and obj == self.one_input:
                    self.select_folder(obj)
                    return True
                elif self.select_os.currentText() == 'Adicionar Comando':
                    return True
                elif obj == self.two_input:
                    if self.select_os.currentText() == 'Mover' or self.select_os.currentText() == 'Copiar':
                        self.select_folder(obj)
                    elif self.select_os.currentText() == 'Criar':
                        return True
                    return True
                self.showSelectionMenu(obj)
                return True
        return super().eventFilter(obj, event)

    def showSelectionMenu(self, input_field):
        """Cria e exibe o menu de seleção de arquivo/pasta"""
        menu = QMenu(self)

        action_file = menu.addAction("Selecionar Arquivo")
        action_folder = menu.addAction("Selecionar Pasta")

        action_file.triggered.connect(lambda: self.select_file(input_field))
        action_folder.triggered.connect(lambda: self.select_folder(input_field))

        menu.exec(input_field.mapToGlobal(input_field.rect().bottomLeft()))

    def select_file(self, input_field):
        """Abre o diálogo para selecionar um arquivo"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione um arquivo")
        if file_path:
            input_field.setText(file_path)

    def select_folder(self, input_field):
        """Abre o diálogo para selecionar uma pasta"""
        folder_path = QFileDialog.getExistingDirectory(self, "Selecione uma pasta")
        if folder_path:
            input_field.setText(folder_path)

    def salvar(self):
        if self.one_input.text():
            if self.select_os.currentText() not in ['Adicionar Comando', 'Deletar']:
                if self.two_input.text():
                    texto = self.select_os.currentText()
                    action = {texto: [self.one_input.text(), self.two_input.text()]}
                    self.fun(texto, action )
                else:
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setWindowTitle("Informações")
                    msg_box.setText("Está faltando informações!\nTermine de inserir as informações e insirá!")
                    msg_box.exec()
            else:
                texto = self.select_os.currentText()
                action = {texto: [self.one_input.text()]}
                self.fun(texto, action )
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Informações")
            msg_box.setText("Está faltando informações!\nTermine de inserir as informações e insirá!")
            msg_box.exec()

