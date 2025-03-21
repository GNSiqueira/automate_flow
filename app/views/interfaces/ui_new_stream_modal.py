from qt_core import *
from app.views.ui import Ui
from app.utils.util import *
from app.utils.enums import *
from app.utils.qt_layout import *
from app.utils.qt_table import expanding_header_table
from app.views.interfaces.selection_print import SelectionPrint
from app.views.interfaces.selection_click import SelectionClick
from app.views.interfaces.selection_comand import SelectionCommand
from app.views.interfaces.selection_os import SelectionOs

class Modal_New_Stream(Ui):
    def __init__(self, home_hide_or_show=None):
        super().__init__(alt=800, larg=430, FixedSize=True, layout=Layout.VERTICAL, modal=True)

        self.home = home_hide_or_show

        self.streams = []

        self.type_action = None
        self.type_tigger = TypeTrigger.TIME
        self.action = None
        self.trigger = '01.00'

        self.title_stream = "Not Defined"
        self.setWindowTitle(f"Automate Flow - {self.title_stream}")
        self.setWindowModality(Qt.ApplicationModal)
        center_x, center_y = screen_center(800, 430)
        self.setGeometry(center_x, center_y, 800, 430)
        self.setFixedSize(800, 430)

        self.central_layout = VLayout(margin=15)
        self.central_layout.setSpacing(0)
        self.section = HLayout()
        self.section1 = VLayout(margin=10)

        self.section1_table = QTableWidget(0, 4)
        self.section1_table.setHorizontalHeaderLabels(['Tipo Ação', 'Tipo Gatilho', 'Gatilho', 'Ação'])
        self.section1_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.section1_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.section1_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.section1_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.section1_table.setStyleSheet("""
            QTableWidget::item:selected {
                background-color: #0c2cab;  /* Cor de fundo forte para a linha */
                color: white;               /* Cor do texto quando selecionado */
            }
        """)

        expanding_header_table(self.section1_table, 0, expanding=False)
        expanding_header_table(self.section1_table, 1, expanding=False)
        expanding_header_table(self.section1_table, 2, expanding=True)
        expanding_header_table(self.section1_table, 3, expanding=True)

        self.section2 = VLayout(margin=10)

        self.section2_input_action = QLineEdit(placeholderText='Ação...')
        self.section2_input_action.setEnabled(False)

        self.section2_input_trigger = QLineEdit(placeholderText='Gatilho...')

        self.section2_type_action_label = QLabel("Tipo Ação")
        self.section2_type_action = QComboBox(placeholderText='Selecionar...')
        self.section2_type_action.currentIndexChanged.connect(self.select_type_action)
        for value in TypeAction:
            self.section2_type_action.addItem(value.value, value.name)

        self.section2_spacing = QFrame()
        self.section2_spacing.setFixedHeight(15)
        self.section2_spacing.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.section2_type_trigger_label = QLabel("Tipo de Gatilho")
        self.section2_type_trigger = QComboBox(placeholderText='Selecionar...')
        self.section2_type_trigger.currentIndexChanged.connect(self.select_type_trigger)
        for value in TypeTrigger:
            self.section2_type_trigger.addItem(value.value, value.name)
        self.section2_type_trigger.setCurrentIndex(2)

        self.section2_label_action = QLabel("Ação")
        self.section2_label_trigger = QLabel("Gatilho")

        self.section2_input_trigger.setText('01.00')
        self.section2_input_trigger.textChanged.connect(lambda text = self.section2_input_trigger.text(): self.validade_input(text=text))

        self.section2.setAlignment(Alignment.Top.value)

        self.section_bottom = HLayout(spacing=5)
        self.section_bottom_buttom_delete_action = QPushButton('Deletar Ação!')
        self.section_bottom_buttom_delete_action.clicked.connect(self.deleteStream)
        self.section_bottom_buttom_finish_stream = QPushButton('Finalizar Fluxo!')
        self.section_bottom_buttom_test_stream = QPushButton('Testar Fluxo!')
        self.section_bottom_buttom_add_action = QPushButton('Adicionar Ação!')
        self.section_bottom_buttom_add_action.clicked.connect(self.addStreamToTable)

        # ADICIONANDO AO LAYOUT
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
                        self.action = x, y
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
            self.action = self.section2_input_action.text()


        return super().eventFilter(obj, event)

    def validade_input(self, text):
        try:
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

    def select_type_trigger(self, index):
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

        if not self.section2_input_trigger.signalsBlocked():
            try:
                self.section2_input_trigger.textChanged.disconnect()
            except TypeError:
                pass

        if index == TypeTrigger.IMAGE.name:
            self.type_tigger = TypeTrigger.IMAGE
            self.section2_type_action.setEnabled(False)
            self.section2_input_trigger.setText('')
            self.section2_input_trigger.setPlaceholderText('Selecionar imagem ...')
            self.section2_input_trigger.installEventFilter(self)
            self.section2_input_trigger.setEnabled(True)

        elif index == TypeTrigger.MOUSE.name:
            self.type_tigger = TypeTrigger.MOUSE
            self.trigger = 'Clique do mouse'
            self.section2_type_action.setEnabled(False)
            self.section2_input_trigger.setText('Clique do mouse')
            self.section2_input_trigger.setEnabled(False)
            self.section2_type_action.setEnabled(True)

        elif index == TypeTrigger.KEY.name:
            self.type_tigger = TypeTrigger.KEY
            self.trigger = 'Tecla F1'
            self.section2_type_action.setEnabled(False)
            self.section2_input_trigger.setText('Tecla F1')
            self.section2_input_trigger.setEnabled(False)
            self.section2_type_action.setEnabled(True)

        elif index == TypeTrigger.TIME.name:
            self.type_tigger = TypeTrigger.TIME
            self.section2_input_trigger.setText('00.00')
            self.section2_input_trigger.setEnabled(True)
            self.section2_input_trigger.textChanged.connect(lambda text = self.section2_input_trigger.text(): self.validade_input(text=text))

    def select_type_action(self, index):
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

        elif index == TypeAction.COMAND.name:
            self.type_action = TypeAction.COMAND
            self.section2_input_action.setEnabled(True)

        elif index == TypeAction.LIST.name:
            self.type_action = TypeAction.LIST

        elif index == TypeAction.OS.name:
            self.type_action = TypeAction.OS
            self.section2_input_action.setEnabled(True)

        elif index == TypeAction.WRITE.name:
            self.type_action = TypeAction.WRITE
            self.section2_input_action.setReadOnly(False)
            self.section2_input_action.setEnabled(True)

    def addStreamToTable(self):

        type_action = self.type_action.name if self.type_action else None
        type_trigger = self.type_tigger.name if self.type_tigger else None
        trigger = self.trigger if self.trigger not in ['00.00', '0.00', '.00'] else None
        action = self.section2_input_action.text() if self.section2_input_action.text() != '' else None

        if any(value is None or value == "" for value in [type_action, type_trigger, action, trigger]) or trigger == '00.00':
            QMessageBox.information(self, 'Informação', 'Preencha todas as informações antes de inserir a ação!')
        else:
            rows = self.section1_table.rowCount()
            self.section1_table.insertRow(rows)
            self.section1_table.setItem(rows, 0, QTableWidgetItem(str(type_action)))
            self.section1_table.setItem(rows, 1, QTableWidgetItem(str(type_trigger)))
            self.section1_table.setItem(rows, 2, QTableWidgetItem(str(trigger)))
            self.section1_table.setItem(rows, 3, QTableWidgetItem(str(action)))

            self.section2_type_trigger.setCurrentIndex(2)
            self.section2_type_action.setCurrentIndex(-1)
            self.section2_input_trigger.setText('01.00')
            self.section2_input_action.setText('')
            self.section2_input_action.setEnabled(True)

            stream = {
                'type_trigger': self.type_tigger.name,
                'trigger' : trigger,
                'type_action': self.type_action.name,
                'action': self.action
            }

            self.streams.append(stream)

            print(self.streams)

            self.type_action = None
            self.type_tigger = TypeTrigger.TIME
            self.action = None
            self.trigger = '01.00'

    def deleteStream(self):
        selected = (self.section1_table.selectedItems())

        if selected:
            selected = selected[0].row()
            self.section1_table.removeRow(selected)
            self.streams.pop(selected)

    def closeEvent(self, event):
        self.home.show()
        return super().closeEvent(event)
