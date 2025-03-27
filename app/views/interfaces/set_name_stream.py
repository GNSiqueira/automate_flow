from qt_core import *
from app.views.ui import Ui
from app.utils.enums import Layout
from app.utils.configs import Configs

class SetNameStream(Ui):
    atualizar_info = Signal(str)

    def __init__(self):
        super().__init__(alt=130, larg=230, FixedSize=True, layout=Layout.VERTICAL, modal=True)

        self.input_name = QLineEdit(placeholderText='Digite o nome...')
        self.button_confirm = QPushButton('Confirmar')
        self.button_confirm.clicked.connect(self.confirmar)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)
        layout.addWidget(self.input_name)
        layout.addWidget(self.button_confirm)

        self.setup(layout)

    def confirmar(self):
        arquivos = Configs.arquivo_leitura()
        texto = self.input_name.text().strip()
        for arquivo in arquivos:
            if arquivo[0] == texto:
                QMessageBox.information(None, "Erro no nome!", "Digite outro nome. \nO nome selecionado já está gravado!")
                return False
        self.atualizar_info.emit(texto)
        self.close()
        del self
