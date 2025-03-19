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
        button = QPushButton('Criar comando!')
        button.clicked.connect(lambda checked: self.create_atalho())
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
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        content_widget = QWidget()
        content_widget.setMaximumWidth(300)
        content_layout = VLayout(content_widget, margin=10)
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

    def create_atalho(self):
        self.close()
        CreateCommand(self.fun)

class CreateCommand(Ui):
    def __init__(self, fun):
        super().__init__(alt=500, larg=300, FixedSize=True, modal=True)
        if callable(fun):
            self.fun = fun
        else:
            raise print("Deu erro nessa bosta de função!")

        self.topo = VLayout(margin=5)
        self.label = QLabel('Aqui será mostrado os comandos')
        self.topo_p2 = HLayout(margin=5)
        self.salvar = QPushButton('Salvar!')
        self.salvar.clicked.connect(lambda checked: self.salvar_command())
        self.limpar = QPushButton('Limpar!')
        self.limpar.clicked.connect(lambda checked: self.limpar_command())

        self.selector = []

        commands = {
            'Espaço': ' ',
            'Exclamação': '!',
            'Aspas': '"',
            'Jogo da velha': '#',
            'Cifrão': '$',
            'Porcentagem': '%',
            'E comercial': '&',
            'Apóstrofo': "'",
            'Parêntese esq.': '(',
            'Parêntese dir.': ')',
            'Asterisco': '*',
            'Mais (+)': '+',
            'Vírgula': ',',
            'Menos': '-',
            'Ponto': '.',
            'Barra': '/',
            'Dois pontos': ':',
            'Ponto e vírgula': ';',
            'Menor que': '<',
            'Igual': '=',
            'Maior que': '>',
            'Interrogação': '?',
            'Arroba': '@',
            'Colchete esq.': '',
            'Barra invertida': '\\',
            'Colchete dir.': '',
            'Circunflexo': '^',
            'Subtraço': '_',
            'Acento grave': '`',
            'Chave esq.': '{',
            'Pipe (|)': '|',
            'Chave dir.': '}',
            'Til': '~',
            'Aceitar': 'accept',
            'Adicionar': 'add',
            'Alternar': 'alt',
            'Alt esquerdo': 'altleft',
            'Alt direito': 'altright',
            'Aplicativos': 'apps',
            'Voltar': 'backspace',
            'Voltar navegador': 'browserback',
            'Favoritos': 'browserfavorites',
            'Avançar navegador': 'browserforward',
            'Página inicial': 'browserhome',
            'Atualizar navegador': 'browserrefresh',
            'Buscar': 'browsersearch',
            'Parar navegador': 'browserstop',
            'Caps lock': 'capslock',
            'Limpar': 'clear',
            'Converter': 'convert',
            'Control': 'ctrl',
            'Ctrl esquerdo': 'ctrlleft',
            'Ctrl direito': 'ctrlright',
            'Decimal': 'decimal',
            'Deletar': 'del',
            'Excluir': 'delete',
            'Divisão': 'divide',
            'Para baixo': 'down',
            'Fim': 'end',
            'Enter': 'enter',
            'Escape': 'esc',
            'Escape': 'escape',
            'Executar': 'execute',
            'Função F1': 'f1',
            'Função F2': 'f2',
            'Função F3': 'f3',
            'Função F4': 'f4',
            'Função F5': 'f5',
            'Função F6': 'f6',
            'Função F7': 'f7',
            'Função F8': 'f8',
            'Função F9': 'f9',
            'Função F10': 'f10',
            'Função F11': 'f11',
            'Função F12': 'f12',
            'Final': 'final',
            'Função': 'fn',
            'Hangul': 'hanguel',
            'Hangul': 'hangul',
            'Hanja': 'hanja',
            'Ajuda': 'help',
            'Início': 'home',
            'Inserir': 'insert',
            'Junja': 'junja',
            'Kana': 'kana',
            'Kanji': 'kanji',
            'Lançar app 1': 'launchapp1',
            'Lançar app 2': 'launchapp2',
            'Lançar email': 'launchmail',
            'Selecionar mídia': 'launchmediaselect',
            'Esquerda': 'left',
            'Mudar modo': 'modechange',
            'Multiplicar': 'multiply',
            'Próxima faixa': 'nexttrack',
            'Sem conversão': 'nonconvert',
            'Números 0': 'num0',
            'Números 1': 'num1',
            'Números 2': 'num2',
            'Números 3': 'num3',
            'Números 4': 'num4',
            'Números 5': 'num5',
            'Números 6': 'num6',
            'Números 7': 'num7',
            'Números 8': 'num8',
            'Números 9': 'num9',
            'Bloqueio numérico': 'numlock',
            'Página abaixo': 'pagedown',
            'Página acima': 'pageup',
            'Pausar': 'pause',
            'Play/Pause': 'playpause',
            'Faixa anterior': 'prevtrack',
            'Imprimir': 'print',
            'Tela de impressão': 'printscreen',
            'Prtscr': 'prntscrn',
            'Print': 'prtsc',
            'Prtscr': 'prtscr',
            'Retornar': 'return',
            'Direita': 'right',
            'Bloqueio rolagem': 'scrolllock',
            'Selecionar': 'select',
            'Separador': 'separator',
            'Shift': 'shift',
            'Shift esquerdo': 'shiftleft',
            'Shift direito': 'shiftright',
            'Dormir': 'sleep',
            'Espaço': 'space',
            'Parar': 'stop',
            'Subtrair': 'subtract',
            'Tabulação': 'tab',
            'Para cima': 'up',
            'Diminuir volume': 'volumedown',
            'Mudo': 'volumemute',
            'Aumentar volume': 'volumeup',
            'Windows': 'win',
            'Windows esquerdo': 'winleft',
            'Windows direito': 'winright',
            'Yen': 'yen',
            'Comando': 'command',
            'Opção': 'option',
            'Opção esquerdo': 'optionleft',
            'Opção direito': 'optionright',
            'A': 'a',
            'B': 'b',
            'C': 'c',
            'D': 'd',
            'E': 'e',
            'F': 'f',
            'G': 'g',
            'H': 'h',
            'I': 'i',
            'J': 'j',
            'K': 'k',
            'L': 'l',
            'M': 'm',
            'N': 'n',
            'O': 'o',
            'P': 'p',
            'Q': 'q',
            'R': 'r',
            'S': 's',
            'T': 't',
            'U': 'u',
            'V': 'v',
            'W': 'w',
            'X': 'x',
            'Y': 'y',
            'Z': 'z'
        }
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        content_widget = QWidget()
        content_widget.setMaximumWidth(300)
        content_layout = VLayout(content_widget, margin=10)
        self.select = None
        for command_desk, command_ata in commands.items():
            button = QPushButton(command_desk)
            button.clicked.connect(lambda checked, key=command_ata : self.adicionar_keys(key))
            content_layout.addWidget(button)



        scroll_area.setWidget(content_widget)


        self.topo.addWidget(self.label)
        self.topo_p2.addWidget(self.limpar)
        self.topo_p2.addWidget(self.salvar)
        self.topo.addLayout(self.topo_p2)



        self.setup(self.topo)
        self.setup(scroll_area)

        self.show()

    def adicionar_keys(self, key):
        self.selector.append(key)
        texto = " + ".join([f"'{str(seletor)}'" for seletor in self.selector])

        self.label.setText(texto)

    def limpar_command(self):
        self.label.setText('Aqui será mostrado os comandos')
        self.selector = []

    def salvar_command(self):
        texto = " + ".join([f"'{str(seletor)}'" for seletor in self.selector])

        self.fun(texto, self.selector)
        self.close()
