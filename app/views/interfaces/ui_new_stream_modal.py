from typing import Literal
from qt_core import *
from app.views.ui import Ui
from app.utils.util import *
from app.utils.enums import *
from app.utils.configs import Configs
from app.utils.qt_layout import *
from app.utils.qt_table import expanding_header_table
from app.views.interfaces.selection_print import SelectionPrint
from app.views.interfaces.selection_click import SelectionClick
from app.views.interfaces.selection_comand import SelectionCommand
from app.views.interfaces.selection_os import SelectionOs
from app.views.interfaces.set_name_stream import SetNameStream
from app.utils.pyautogui_controller import Trigger, Action

class Modal_New_Stream(Ui):

    atualizar_info = Signal()

    def __init__(self, home_hide_or_show=None, streams = None):
        super().__init__(alt=800, larg=430, FixedSize=True, layout=Layout.VERTICAL, modal=True)

        self.home = home_hide_or_show

        if streams:
            self.streams_total = Configs.arquivo_leitura()
            self.streams = self.streams_total[streams- 1]
        else:
            self.streams = ['Not Defined!']

        self.type_action = None
        self.type_trigger = TypeTrigger.TIME
        self.action = None
        self.trigger = '00.05'


        self.setWindowTitle(f"Automate Flow - {self.streams[0]}")
        self.setWindowModality(Qt.ApplicationModal)
        center_x, center_y = screen_center(800, 430)
        self.setGeometry(center_x, center_y, 800, 430)
        self.setFixedSize(800, 430)

        self.central_layout = VLayout(margin=15)
        self.central_layout.setSpacing(0)
        self.section = HLayout()
        self.section1 = VLayout(margin=10)

        self.butons_superior = HLayout(spacing=5, margin=10)

        self.up = QPushButton('Up')
        self.up.clicked.connect(lambda: self.alterarOrdem('up'))
        self.down = QPushButton('Down')
        self.down.clicked.connect(lambda: self.alterarOrdem('down'))

        self.section1_table = QTableWidget(0, 4)
        self.section1_table.setHorizontalHeaderLabels(['Tipo Ação', 'Tipo Gatilho', 'Gatilho', 'Ação'])

        # Define que a tabela não permite seleção de células ou linhas
        self.section1_table.setSelectionMode(QAbstractItemView.NoSelection)
        # Impede a edição direta dos itens da tabela
        self.section1_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Faz com que, ao selecionar um item, a linha inteira seja selecionada
        self.section1_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Define que apenas uma linha pode ser selecionada por vez (substitui NoSelection anterior)
        self.section1_table.setSelectionMode(QAbstractItemView.SingleSelection)
        # Define o estilo da seleção (cor de fundo e cor do texto ao selecionar uma linha)
        self.section1_table.setStyleSheet("""
            QTableWidget::item:selected {
                background-color: #0c2cab;  /* Cor de fundo azul forte para a linha selecionada */
                color: white;               /* Cor do texto ao selecionar */

            }
        """)

        if streams:
            for c, a in enumerate(self.streams[1:]):
                self.section1_table.insertRow(c)
                self.section1_table.setItem(c, 0, QTableWidgetItem(str(a['type_action'])))
                self.section1_table.setItem(c, 1, QTableWidgetItem(str(a['type_trigger'])))
                self.section1_table.setItem(c, 2, QTableWidgetItem(str(a['trigger'])))
                self.section1_table.setItem(c, 3, QTableWidgetItem(str(a['action'][0])))

        self.section1_table.cellDoubleClicked.connect(self.selectTableEdit)

        expanding_header_table(self.section1_table, 0, expanding=False)
        expanding_header_table(self.section1_table, 1, expanding=False)
        expanding_header_table(self.section1_table, 2, expanding=True)
        expanding_header_table(self.section1_table, 3, expanding=True)

        self.section1_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.section1_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.section2 = VLayout(margin=10)

        self.section2_input_action = QLineEdit(placeholderText='Ação...')
        self.section2_input_action.setEnabled(False)

        self.section2_input_trigger = QLineEdit(placeholderText='Gatilho...')

        self.section2_type_action_label = QLabel("Tipo Ação")
        self.section2_type_action = QComboBox(placeholderText='Selecionar...')
        self.section2_type_action.currentIndexChanged.connect(self.selectTypeAction)
        for value in TypeAction:
            self.section2_type_action.addItem(value.value, value.name)

        self.section2_spacing = QFrame()
        self.section2_spacing.setFixedHeight(15)
        self.section2_spacing.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.section2_type_trigger_label = QLabel("Tipo de Gatilho")
        self.section2_type_trigger = QComboBox(placeholderText='Selecionar...')
        self.section2_type_trigger.currentIndexChanged.connect(self.selectTypeTrigger)
        for value in TypeTrigger:
            self.section2_type_trigger.addItem(value.value, value.name)
        self.section2_type_trigger.setCurrentIndex(2)

        self.section2_label_action = QLabel("Ação")
        self.section2_label_trigger = QLabel("Gatilho")

        self.section2_input_trigger.setText('00.05')
        self.section2_input_trigger.textChanged.connect(self.validadeInput)

        self.section2.setAlignment(Alignment.Top.value)

        self.section_bottom = HLayout(spacing=5)
        self.section_bottom_buttom_delete_action = QPushButton('Deletar Ação!')
        self.section_bottom_buttom_delete_action.clicked.connect(self.deleteStream)
        self.section_bottom_buttom_finish_stream = QPushButton('Finalizar Fluxo!')
        self.section_bottom_buttom_finish_stream.clicked.connect(self.finatityStream if not streams else self.updateStream)
        self.section_bottom_buttom_test_stream = QPushButton('Testar Fluxo!')
        self.section_bottom_buttom_test_stream.clicked.connect(self.testeStream)
        self.section_bottom_buttom_add_action = QPushButton('Adicionar Ação!')
        self.section_bottom_buttom_add_action.clicked.connect(self.addStreamToTable)

        # ADICIONANDO AO LAYOUT
        self.butons_superior.addWidget(self.up)
        self.butons_superior.addWidget(self.down)

        self.section1.addLayout(self.butons_superior)
        self.section1.addWidget(self.section1_table)

        self.section2.addWidget(self.section2_type_trigger_label)
        self.section2.addWidget(self.section2_type_trigger)
        self.section2.addWidget(self.section2_spacing)
        self.section2.addWidget(self.section2_label_trigger)
        self.section2.addWidget(self.section2_input_trigger)
        self.section2.addWidget(self.section2_spacing)
        self.section2.addWidget(self.section2_type_action_label)
        self.section2.addWidget(self.section2_type_action)
        self.section2.addWidget(self.section2_spacing)
        self.section2.addWidget(self.section2_label_action)
        self.section2.addWidget(self.section2_input_action)

        self.section_bottom.addWidget(self.section_bottom_buttom_delete_action)
        self.section_bottom.addWidget(self.section_bottom_buttom_test_stream)
        self.section_bottom.addWidget(self.section_bottom_buttom_finish_stream)
        self.section_bottom.addWidget(self.section_bottom_buttom_add_action)

        self.section.addLayout(self.section1, 2)
        self.section.addLayout(self.section2, 1)

        self.central_layout.addLayout(self.section)
        self.central_layout.addLayout(self.section_bottom)

        self.setup(self.central_layout)
    # ====================================================================================
    #                                FUNCTION TO CLASS
    # ====================================================================================
    def eventFilter(self, obj, event):
        """
            Objetivo da função é ser acionado assim que algum evendo for usado em alguma parte do sistema(Apenas se for instalado)

            + Se o evento for, precionar o mouse && o objeto for o Input Trigger
                Irá abrir a janela de print.
        """
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj == self.section2_input_trigger:
                windows_screen = []
                from app import app
                def finalityPrint(text):
                    self.show()
                    self.section2_input_trigger.setText(text)
                    self.trigger = text
                    self.section2_type_action.setEnabled(True)
                self.hide()
                for screen in app.screens():
                    screen_geometry = screen.geometry()
                    window = SelectionPrint(screen_geometry, fun=finalityPrint)
                    windows_screen.append(window)
                for window in windows_screen:
                    window.set_windows(windows_screen)
                    window.show()
                self.section2_input_trigger.removeEventFilter(self)
                return True

            elif obj == self.section2_input_action:
                if self.type_action == TypeAction.CLICK:
                    from app import app
                    def finalityClick(text, x, y):
                        self.section2_input_action.setText(text)
                        self.cordenadas_x = x
                        self.cordenadas_y = y
                        self.action = text, x, y
                        self.show()
                        pass
                    windows = []
                    self.hide()
                    for screen in app.screens():
                        screen_geometry = screen.geometry()
                        window = SelectionClick(screen_geometry, windows, screen_geometry.x(), screen_geometry.y(), fun=finalityClick)
                        windows.append(window)
                    self.section2_input_action.removeEventFilter(self)
                    self.section2_input_action.setEnabled(False)

                elif self.type_action == TypeAction.COMAND:
                    def finalityCommand(text, input_action):
                        self.section2_input_action.setText(text)
                        self.action = input_action
                        self.action.insert(1, 1)
                        self.opcoesAlternar(alt=True)
                    SelectionCommand(finalityCommand)

                elif self.type_action == TypeAction.OS:
                    def finalityOs(text, input_action):
                        self.section2_input_action.setText(text)
                        self.action = input_action
                        self.selectionOs.deleteLater()
                    self.selectionOs = SelectionOs(finalityOs)
                    self.selectionOs.show()
                return True

        elif event.type() == QEvent.Type.KeyRelease:
            self.action = [self.section2_input_action.text()]


        return super().eventFilter(obj, event)

    def validadeInput(self):
        try:
            text = self.section2_input_trigger.text()
            numero = float(text)
            texto = text.replace('.', '')
            texto = texto[:-2] + '.' + texto[-2:]
            if texto[0] == '0' and len(texto) != 5:
                texto = texto[1:]
            elif len(texto) == 4:
                texto = '0' + texto
            elif len(texto) == 3:
                texto = '00' + texto

            if len(texto) != 5 and texto[:2] == '00':
                for num in texto:
                    if num == '0':
                        texto = texto[1:]
                    else:
                        break

            if texto != '00.00':
                self.section2_type_action.setEnabled(True)
            else:
                self.section2_type_action.setEnabled(False)
                self.section2_input_action.setEnabled(False)

            self.section2_input_trigger.setText(texto)
            self.trigger = texto
        except:
            self.section2_input_trigger.setText('00.00')

    def selectTypeTrigger(self, index):
        '''
            O objetivo dessa função é identificar qual tipo de gatinho foi selecionado

            + Se for Image:
                O deve definir a função de click do input como abrir o print.
                Deve ser ao clicar no input e será aberto uma janela se seleção.
                Assim que for feito ação de print, ativara a seleção do Tipo Ação.

            + Se for MOUSE:
                Colocar o texto do input como click.
                Deixar ele inativo.
                Ativar a seleção do Tipo Ação

            + Se for KEY:
                Colocar o texto do input como tecla.
                Deixar ele inativo.
                Ativar a seleção do tipo Ação.

            + Se for TIME:
                Deixar com que escreva no input(apenas inteiro, e float até 2 numeros depois da virgula).
                Colocar ação que assim que escrever e for correto o tipo, ativar a seleção do Tipo Ação.
        '''
        self.section2_input_trigger.setEnabled(False)

        index = self.section2_type_trigger.itemData(index)

        self.trigger = None

        if self.section2_input_trigger.hasMouseTracking():
            self.section2_input_trigger.removeEventFilter(self)

        try:
            self.section2_input_trigger.textChanged.disconnect()
        except RuntimeError:
            pass  # Ignora se o sinal não estiver conectado

        if index == TypeTrigger.IMAGE.name:
            self.type_trigger = TypeTrigger.IMAGE
            self.section2_type_action.setEnabled(False)
            self.section2_input_trigger.setText('')
            self.section2_input_trigger.setPlaceholderText('Selecionar imagem ...')
            self.section2_input_trigger.installEventFilter(self)
            self.section2_input_trigger.setEnabled(True)

        elif index == TypeTrigger.MOUSE.name:
            self.type_trigger = TypeTrigger.MOUSE
            self.trigger = 'Clique do mouse'
            self.section2_type_action.setEnabled(False)
            self.section2_input_trigger.setText('Clique do mouse')
            self.section2_input_trigger.setEnabled(False)
            self.section2_type_action.setEnabled(True)

        elif index == TypeTrigger.KEY.name:
            self.type_trigger = TypeTrigger.KEY
            self.trigger = 'Tecla Ctrl'
            self.section2_type_action.setEnabled(False)
            self.section2_input_trigger.setText('Tecla Ctrl')
            self.section2_input_trigger.setEnabled(False)
            self.section2_type_action.setEnabled(True)

        elif index == TypeTrigger.TIME.name:
            self.type_trigger = TypeTrigger.TIME
            self.section2_input_trigger.setText('00.00')
            self.section2_input_trigger.setEnabled(True)
            self.section2_type_action.setEnabled(False)
            self.section2_input_trigger.textChanged.connect(self.validadeInput)

    def selectTypeAction(self, index):
        '''
            O Objetivo dessa função é identificar qual tipo de ação é escolhido e fazer uma ação com base nisso.

            + CLICK: Se for Clique tem que abrir a janela para clicar quando for clicado no input.
            + COMMAND: Deve abrir uma janela com a seleção dos comandos e talvez até adicionar um comando.
        '''
        self.section2_input_action.installEventFilter(self)
        index = self.section2_type_action.itemData(index)
        self.section2_input_action.setText('')
        self.section2_input_action.setReadOnly(True)

        if index == TypeAction.CLICK.name:
            self.type_action = TypeAction.CLICK
            self.section2_input_action.setEnabled(True)
            self.opcoesAlternar()

        elif index == TypeAction.COMAND.name:
            self.type_action = TypeAction.COMAND
            self.section2_input_action.setEnabled(True)
            self.opcoesAlternar()

        elif index == TypeAction.OS.name:
            self.type_action = TypeAction.OS
            self.section2_input_action.setEnabled(True)
            self.opcoesAlternar()

        elif index == TypeAction.WRITE.name:
            self.type_action = TypeAction.WRITE
            self.section2_input_action.setReadOnly(False)
            self.section2_input_action.setEnabled(True)
            self.opcoesAlternar(alt=True)


    def addStreamToTable(self):

        type_action = self.type_action.name if self.type_action else None
        type_trigger = self.type_trigger.name if self.type_trigger else None
        trigger = self.trigger if self.trigger not in ['00.00', '0.00', '.00'] else None
        action = self.section2_input_action.text() if self.section2_input_action.text() != '' else None

        if any(value is None or value == "" for value in [type_action, type_trigger, action, trigger]) or trigger == '00.00':
            QMessageBox.information(self, 'Informação', 'Preencha todas as informações antes de inserir a ação!')
            return False
        else:
            rows = self.section1_table.rowCount()
            self.section1_table.insertRow(rows)
            self.section1_table.setItem(rows, 0, QTableWidgetItem(str(type_action)))
            self.section1_table.setItem(rows, 1, QTableWidgetItem(str(type_trigger)))
            self.section1_table.setItem(rows, 2, QTableWidgetItem(str(trigger)))
            self.section1_table.setItem(rows, 3, QTableWidgetItem(str(action)))

            self.section2_type_trigger.setCurrentIndex(2)
            self.section2_type_action.setCurrentIndex(-1)
            self.section2_input_trigger.setText('00.05')
            self.section2_input_action.setText('')
            self.section2_input_action.setEnabled(True)

            stream = {
                'type_trigger': type_trigger,
                'trigger' : trigger,
                'type_action': type_action,
                'action': self.action
            }

            self.streams.append(stream)

            if self.type_action == TypeAction.WRITE:
                if self.option_enter.isChecked() == True:
                    stream = {
                        'type_trigger': 'TIME',
                        'trigger' : '00.05',
                        'type_action': 'COMAND',
                        'action': ['Enter',"1", 'enter']
                    }
                    self.streams.append(stream)
                    self.section1_table.insertRow(rows + 1)
                    self.section1_table.setItem(rows + 1, 0, QTableWidgetItem('COMAND'))
                    self.section1_table.setItem(rows + 1, 1, QTableWidgetItem('TIME'))
                    self.section1_table.setItem(rows + 1, 2, QTableWidgetItem('00.05'))
                    self.section1_table.setItem(rows + 1, 3, QTableWidgetItem('Enter'))
                elif self.option_tab.isChecked() == True:
                    stream = {
                        'type_trigger': 'TIME',
                        'trigger' : '00.05',
                        'type_action': 'COMAND',
                        'action': ['Tab', "1", 'tab']
                    }
                    self.streams.append(stream)
                    self.section1_table.insertRow(rows + 1)
                    self.section1_table.setItem(rows + 1, 0, QTableWidgetItem('COMAND'))
                    self.section1_table.setItem(rows + 1, 1, QTableWidgetItem('TIME'))
                    self.section1_table.setItem(rows + 1, 2, QTableWidgetItem('00.05'))
                    self.section1_table.setItem(rows + 1, 3, QTableWidgetItem('Tab'))

            self.type_trigger = TypeTrigger.TIME
            self.action = None
            self.trigger = '00.05'
            self.type_action = None

            self.opcoesAlternar()

        return True

    def updateStreamToTable(self):
        if not self.linha:
            self.section_bottom_buttom_add_action.setText('Adicionar Ação!')
            self.section_bottom_buttom_add_action.clicked.disconnect()
            self.section_bottom_buttom_add_action.clicked.connect(self.addStreamToTable)
            return False
        type_action = self.type_action.name if self.type_action else None
        type_trigger = self.type_trigger.name if self.type_trigger else None
        trigger = self.trigger if self.trigger not in ['00.00', '0.00', '.00'] else None
        action = self.section2_input_action.text() if self.section2_input_action.text() != '' else None

        if any(value is None or value == "" for value in [type_action, type_trigger, action, trigger]) or trigger == '00.00':
            QMessageBox.information(self, 'Informação', 'Preencha todas as informações antes de inserir a ação!')
            return False
        else:
            self.section1_table.setItem(self.linha -  1, 0, QTableWidgetItem(str(type_action)))
            self.section1_table.setItem(self.linha -  1, 1, QTableWidgetItem(str(type_trigger)))
            self.section1_table.setItem(self.linha -  1, 2, QTableWidgetItem(str(trigger)))
            self.section1_table.setItem(self.linha -  1, 3, QTableWidgetItem(str(action)))

            self.section2_type_trigger.setCurrentIndex(2)
            self.section2_type_action.setCurrentIndex(-1)
            self.section2_input_trigger.setText('00.05')
            self.section2_input_action.setText('')
            self.section2_input_action.setEnabled(True)

            stream = {
                'type_trigger': type_trigger,
                'trigger' : trigger,
                'type_action': type_action,
                'action': self.action
            }

            self.streams[self.linha] = stream

            self.type_action = None
            self.type_trigger = TypeTrigger.TIME
            self.action = None
            self.trigger = '00.05'

            self.section_bottom_buttom_add_action.setText('Adicionar Ação!')
            self.section_bottom_buttom_add_action.clicked.disconnect()
            self.section_bottom_buttom_add_action.clicked.connect(self.addStreamToTable)

        return True

    def deleteStream(self):
        selected = (self.section1_table.selectedItems())

        if selected:
            selected = selected[0].row()
            self.section1_table.removeRow(selected)
            self.streams.pop(selected)

    def finatityStream(self):
        if len(self.streams) < 2:
            QMessageBox.information(None, "Informação", "Insirá no minimo uma ação nesse fluxo!")
            return False

        def set_name_stream(name):
            self.streams[0] = name
            arquivo = Configs.arquivo_leitura()
            arquivo.append(self.streams)
            Configs.arquivo_escrita(arquivo)
            self.close()

        self.set_name = SetNameStream()
        self.set_name.atualizar_info.connect(set_name_stream)
        self.set_name.show()

    def updateStream(self):
        if len(self.streams) < 2:
            QMessageBox.information(None, "Informação", "Insirá no minimo uma ação nesse fluxo!")
            return False

        Configs.arquivo_escrita(self.streams_total)
        self.close()

    def selectTableEdit(self, row):
        self.section_bottom_buttom_add_action.setText('Alterar fluxo!')
        self.section_bottom_buttom_add_action.clicked.disconnect()
        self.section_bottom_buttom_add_action.clicked.connect(self.updateStreamToTable)

        self.linha = row + 1

        # Definindo inputs
        self.type_trigger = self.streams[self.linha]['type_trigger']
        for c in TypeTrigger:
            if c.name == self.type_trigger:
                self.type_trigger = c
                break

        self.type_action = self.streams[self.linha]['type_action']
        for c in TypeAction:
            if c.name == self.type_action:
                self.type_action = c
                break

        self.trigger = self.streams[self.linha]['trigger']
        self.action = self.streams[self.linha]['action']

        trigger = self.trigger

        # Type Trigger
        for n, c in enumerate(TypeTrigger):
            if str(c.name) == str(self.type_trigger.name):
                self.section2_type_trigger.setCurrentIndex(n)
                break

        for n, c in enumerate(TypeAction):
            if str(c.name) == str(self.type_action.name):
                self.section2_type_action.setCurrentIndex(n)
                break


        self.trigger = trigger
        self.section2_input_trigger.setText(trigger)

        self.section2_input_action.setText(self.action[0])

    def closeEvent(self, event):
        self.atualizar_info.emit()
        self.home.show()
        return super().closeEvent(event)

    def testeStream(self):
        try:
            self.hide()

            for stream in self.streams[1:]:
                Trigger(stream['type_trigger'], stream['trigger'])
                Action(stream['type_action'], stream['action'])

            self.show()
        except TypeError as e:
            self.show()
            print(e)
            QMessageBox.information(None, 'Informação', 'Erro ao executar fluxo!')

    def opcoesAMaisWrite(self):
        self.group_button_1 = QButtonGroup()

        self.option_enter = QRadioButton('Enter')
        self.option_tab = QRadioButton('Tab')

        self.group_button_1.addButton(self.option_enter)
        self.group_button_1.addButton(self.option_tab)

        self.section2_options = HLayout(margin=20)
        self.section2_options.addWidget(self.option_enter)
        self.section2_options.addWidget(self.option_tab)

        self.section2.addLayout(self.section2_options)

    def opcoesAMaisComand(self):
        self.option_comand = VLayout(margin=15, spacing=15)
        self.action[1] = 1
        self.option_label = QLabel(f"Quantidade de execução: {self.action[1]}")
        self.option_mais = QPushButton('Mais')
        self.option_menos = QPushButton('Menos')
        self.option_comand_horizontal = HLayout(spacing=5)

        def mais():
            self.action[1] += 1
            self.option_label.setText(f"Quantidade de execução: {self.action[1]}")

        def menos():
            if self.action[1] > 1:
                self.action[1] -= 1
                self.option_label.setText(f"Quantidade de execução: {self.action[1]}")

        self.option_mais.clicked.connect(lambda: mais())
        self.option_menos.clicked.connect(lambda: menos())


        self.option_comand_horizontal.addWidget(self.option_menos)
        self.option_comand_horizontal.addWidget(self.option_mais)

        self.option_comand.addWidget(self.option_label)
        self.option_comand.addLayout(self.option_comand_horizontal)

        self.section2.addLayout(self.option_comand)

    def opcoesAlternar(self, alt = None):
        if hasattr(self, 'option_comand') and self.option_comand:
            while self.option_comand_horizontal.count():
                item = self.option_comand_horizontal.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.section2.removeItem(self.option_comand_horizontal)
            while self.option_comand.count():
                item = self.option_comand.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.section2.removeItem(self.option_comand)

            if hasattr(self, 'option_comand'):
                del self.option_comand
            if hasattr(self, 'option_label'):
                del self.option_label
            if hasattr(self, 'option_mais'):
                del self.option_mais
            if hasattr(self, 'option_menos'):
                del self.option_menos
            if hasattr(self, 'option_comand_horizontal'):
                del self.option_comand_horizontal

        elif hasattr(self, 'section2_options') and self.section2_options:
            while self.section2_options.count():
                item = self.section2_options.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.section2.removeItem(self.section2_options)
            del self.section2_options

            if hasattr(self, 'grup_button_1'):
                del self.grup_button_1
            if hasattr(self, 'option_enter'):
                del self.option_enter
            if hasattr(self, 'option_tab'):
                del self.option_tab

        if alt == True:
            if self.type_action == TypeAction.WRITE:
                self.opcoesAMaisWrite()

            elif self.type_action == TypeAction.COMAND:
                self.opcoesAMaisComand()


    def alterarOrdem(self, ordem:Literal['up', 'down']):
        select = self.section1_table.selectedItems()

        if select:
            select = int(select[0].row() + 1)

            if ordem == 'up' and select > 1:
                atual = {
                    'type_trigger': self.streams[select]['type_trigger'],
                    'trigger' : self.streams[select]['trigger'],
                    'type_action': self.streams[select]['type_action'],
                    'action': self.streams[select]['action']
                }

                superior = {
                    'type_trigger': self.streams[select - 1]['type_trigger'],
                    'trigger' : self.streams[select - 1]['trigger'],
                    'type_action': self.streams[select - 1]['type_action'],
                    'action': self.streams[select - 1]['action']
                }
                self.streams[select] = superior
                self.streams[select - 1] = atual

                select -= 1
                self.section1_table.setCurrentCell(select - 1, 0)

                self.section1_table.setItem(select, 0, QTableWidgetItem(str(superior['type_action'])))
                self.section1_table.setItem(select, 1, QTableWidgetItem(str(superior['type_trigger'])))
                self.section1_table.setItem(select, 2, QTableWidgetItem(str(superior['trigger'])))
                self.section1_table.setItem(select, 3, QTableWidgetItem(str(superior['action'][0])))

                self.section1_table.setItem(select - 1, 0, QTableWidgetItem(str(atual['type_action'])))
                self.section1_table.setItem(select - 1, 1, QTableWidgetItem(str(atual['type_trigger'])))
                self.section1_table.setItem(select - 1, 2, QTableWidgetItem(str(atual['trigger'])))
                self.section1_table.setItem(select - 1, 3, QTableWidgetItem(str(atual['action'][0])))

            elif ordem == 'down':
                atual = {
                    'type_trigger': self.streams[select]['type_trigger'],
                    'trigger' : self.streams[select]['trigger'],
                    'type_action': self.streams[select]['type_action'],
                    'action': self.streams[select]['action']
                }

                inferior = {
                    'type_trigger': self.streams[select + 1]['type_trigger'],
                    'trigger' : self.streams[select + 1]['trigger'],
                    'type_action': self.streams[select + 1]['type_action'],
                    'action': self.streams[select + 1]['action']
                }
                self.streams[select] = inferior
                self.streams[select + 1] = atual

                select -= 1
                self.section1_table.setCurrentCell(select + 1, 0)

                self.section1_table.setItem(select, 0, QTableWidgetItem(str(inferior['type_action'])))
                self.section1_table.setItem(select, 1, QTableWidgetItem(str(inferior['type_trigger'])))
                self.section1_table.setItem(select, 2, QTableWidgetItem(str(inferior['trigger'])))
                self.section1_table.setItem(select, 3, QTableWidgetItem(str(inferior['action'][0])))

                self.section1_table.setItem(select + 1, 0, QTableWidgetItem(str(atual['type_action'])))
                self.section1_table.setItem(select + 1, 1, QTableWidgetItem(str(atual['type_trigger'])))
                self.section1_table.setItem(select + 1, 2, QTableWidgetItem(str(atual['trigger'])))
                self.section1_table.setItem(select + 1, 3, QTableWidgetItem(str(atual['action'][0])))


