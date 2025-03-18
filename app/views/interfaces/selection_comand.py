from app.views.ui import Ui
from app.utils.enums import Layout
from qt_core import *
from app.utils.qt_layout import VLayout, HLayout

class SelectionCommand(Ui):
    def __init__(self, fun):
        super().__init__(alt=500, larg=300, FixedSize=True, layout=Layout.VERTICAL, modal=True)

        if callable(fun):
            self.fun = fun
        else:
            raise print("Esta merda tem que ser uma função!")

        self.topo = HLayout(margin=5)
        input_search = QLineEdit(placeholderText='Inserir comando!')
        button = QPushButton('Salvar')
        self.topo.addWidget(input_search)
        self.topo.addWidget(button)

        comands = {
            # Manipulação de texto
            'Copiar': ['ctrl', 'c'],
            'Cortar': ['ctrl', 'x'],
            'Colar': ['ctrl', 'v'],
            'Colar especial': ['shift', 'insert'],
            'Desfazer': ['ctrl', 'z'],
            'Refazer': ['ctrl', 'y'],
            'Selecionar tudo': ['ctrl', 'a'],

            # Navegação (janelas e abas)
            'Alterar janela': ['alt', 'tab'],
            'Explorador de arquivos': ['win', 'e'],
            'Fechar programa': ['alt', 'f4'],
            'Abrir o Explorador de Tarefas (Visão de Tarefas)': ['win', 'tab'],
            'Minimizar todas as janelas': ['win', 'd'],
            'Bloquear tela': ['win', 'l'],
            'Reabrir aba fechada (Navegador)': ['ctrl', 'shift', 't'],
            'Fechar aba (Navegador)': ['ctrl', 'w'],
            'Guia anônima (Navegador)': ['ctrl', 'shift', 'n'],
            'Nova aba (Navegador)': ['ctrl', 'c'],  # Talvez revisar esse atalho!

            # Comandos específicos do Windows
            'Abrir configurações do sistema': ['win', 'i'],
            'Abrir Gerenciador de Tarefas': ['ctrl', 'shift', 'esc'],
            'Abrir histórico de área de transferência': ['win', 'v'],
            'Abrir a linha de comando (Executar)': ['win', 'r'],
            'Abrir Barra de Emojis': ['win', '.'],  # ou ['win', ';']

            # Outros comandos úteis
            'Tab para cima': ['shift', 'tab'],
            'Tab': ['tab'],
            'Seta para baixo': ['down'],
            'Seta para cima': ['up'],
            'Seta para a esquerda': ['left'],
            'Seta para a direita': ['right'],
            'Espaço': ['space'],
            'Windows': ['win']
        }

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = VLayout(content_widget)
        self.select = None
        for command_desk, command_ata in comands.items():
            button = QPushButton(command_desk)
            button.clicked.connect(lambda checked, keys=command_ata, cmd = command_desk: self.on_button_click(keys, cmd))
            content_layout.addWidget(button)

        scroll_area.setWidget(content_widget)

        self.setup(self.topo)
        self.setup(scroll_area)

        self.show()

    def on_button_click(self, keys, cmd):
        self.fun(cmd, keys)
        self.close()
