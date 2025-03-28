from app.views.ui import Ui
from app.utils.enums import Layout
from qt_core import *
from app.utils.qt_layout import *
from app.utils.configs import Configs
from app.views.interfaces.ui_home import Home

class NewConfigs(Ui):
    def __init__(self):
        super().__init__(alt=130, larg=250, FixedSize=False, layout=Layout.VERTICAL, modal=True)

        self.main_layout = VLayout(margin=15, spacing=10)

        label_computador = QLabel('Deseja salvar as configurações no computador?')
        self.button_computador = QPushButton('Sim')

        label_existente = QLabel('O arquivo de configurações ja existe? Onde está?')
        self.button_existente = QPushButton('Sim')

        label_diferente = QLabel('Deseja salvar em outro local?')
        self.button_diferente = QPushButton('Sim')

        label_local = QLabel('Deseja salvar as configurações na pasta atual?')
        self.button_local = QPushButton('Sim')

        self.main_layout.addWidget(label_computador)
        self.main_layout.addWidget(self.button_computador)

        self.main_layout.addWidget(label_existente)
        self.main_layout.addWidget(self.button_existente)

        self.main_layout.addWidget(label_diferente)
        self.main_layout.addWidget(self.button_diferente)

        self.main_layout.addWidget(label_local)
        self.main_layout.addWidget(self.button_local)

        self.button_diferente.clicked.connect(self.diferente)
        self.button_existente.clicked.connect(self.existente)
        self.button_local.clicked.connect(self.local)
        self.button_computador.clicked.connect(self.computador)

        self.setup(self.main_layout)

        self.verificar()

    def diferente(self):
        self.hide()
        path = QFileDialog.getExistingDirectory(self, 'Selecionar local para salvar!')
        if path:
            Configs.diferente(path)
            self.verificar()
        else:
            self.show()
            QMessageBox.information(None, 'Informação', 'Selecione a pasta que deseja salvar!')

    def existente(self):
        self.hide()
        path = QFileDialog.getExistingDirectory(self, 'Selecionar local existente!')
        if path:
            Configs.existente(path)
            self.verificar()
        else:
            self.show()
            QMessageBox.information(None, 'Informação', 'Selecione a pasta que deseja salvar!')


    def local(self):
        Configs.local()
        self.verificar()

    def computador(self):
        Configs.computador()
        self.verificar()

    def verificar(self):
        if Configs.repositories():
            self.close()
        else:
            self.show()

    def closeEvent(self, event):
        if Configs.repositories() == False:
            return
        self.home = Home()
        self.home.show()
        return super().closeEvent(event)

