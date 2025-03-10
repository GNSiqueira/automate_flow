from qt_core import * 
from app.views.ui import Ui
from app.utils.util import *
from app.utils.enums import *
from app.utils.qt_layout import *
from app.utils.qt_table import expanding_header_table
from app.views.interfaces.selection_print import SelectionPrint
from app.views.interfaces.selection_click import SelectionClick

class Modal_New_Stream(QMainWindow): 
    def __init__(self, parent=None):
        super().__init__()

        self.home = parent
        self.type_trigger = None

        self.title_stream = "Not Defined"
        self.setWindowTitle(f"Automate Flow - {self.title_stream}")
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(800, 430)
        
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.setContentsMargins(15,15,15,15)
        self.central_layout.setSpacing(0)
        self.section = HLayout()
        self.section1 = VLayout(margin=10)

        self.section1_table = QTableWidget(3, 4)
        self.section1_table.setHorizontalHeaderLabels(['Tipo Ação', 'Tipo Gatilho', 'Gatilho', 'Ação'])

        expanding_header_table(self.section1_table, 0, expanding=False)
        expanding_header_table(self.section1_table, 1, expanding=False)
        expanding_header_table(self.section1_table, 2, expanding=True)
        expanding_header_table(self.section1_table, 3, expanding=True)

        self.section2 = VLayout(margin=10)


        self.section2_type_action_label = QLabel("Tipo Ação")
        self.section2_type_action = QComboBox(placeholderText='Selecionar...')
        self.section2_type_action.setEnabled(False)
        self.section2_type_action.currentIndexChanged.connect(self.active_action)
        for value in TypeAction: 
            self.section2_type_action.addItem(value.value, value.name)
        
        self.section2_spacing = QFrame() 
        self.section2_spacing.setFixedHeight(15)
        self.section2_spacing.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.section2_type_trigger_label = QLabel("Tipo de Gatilho")
        self.section2_type_trigger = QComboBox(placeholderText='Selecionar...')
        self.section2_type_trigger.currentIndexChanged.connect(self.active_trigger)
        for value in TypeTrigger:
            self.section2_type_trigger.addItem(value.value, value.name)

        self.section2_label_action = QLabel("Ação")
        self.section2_label_trigger = QLabel("Gatilho")
        
        self.section2_input_trigger = QLineEdit(placeholderText='Gatilho...')
        self.section2_input_trigger.mousePressEvent = self.input_trigger()
        self.section2_input_trigger.setEnabled(False)
        
        self.section2_input_action = QLineEdit(placeholderText='Ação...')
        self.section2_input_action.setEnabled(False)

        self.section2.setAlignment(Alignment.Top.value)

        self.section_bottom = HLayout(spacing=5)
        self.section_bottom_buttom_delete_action = QPushButton('Deletar Ação!')
        self.section_bottom_buttom_finish_stream = QPushButton('Finalizar Fluxo!')
        self.section_bottom_buttom_test_stream = QPushButton('Testar Fluxo!')
        self.section_bottom_buttom_add_action = QPushButton('Adicionar Ação!')

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
        
        self.section_bottom.addWidget(self.section_bottom_buttom_add_action)
        self.section_bottom.addWidget(self.section_bottom_buttom_delete_action)
        self.section_bottom.addWidget(self.section_bottom_buttom_finish_stream)
        self.section_bottom.addWidget(self.section_bottom_buttom_test_stream)

        self.section.addLayout(self.section1, 2)
        self.section.addLayout(self.section2, 1)

        self.central_layout.addLayout(self.section)
        self.central_layout.addLayout(self.section_bottom)

        self.setCentralWidget(self.central_widget)

    # Ativação do Input Trigger
    def active_trigger(self, index):
        index = self.section2_type_trigger.itemData(index)
        
        if index == TypeTrigger.IMAGE.name:
            self.type_trigger = TypeTrigger.IMAGE
            self.section2_input_trigger.setText('')
            self.section2_input_trigger.setPlaceholderText('Selecionar imagem ...')
            self.section2_input_trigger.setEnabled(True)
            self.section2_type_action.setEnabled(False)
        
        elif index == TypeTrigger.MOUSE.name:
            self.type_trigger = TypeTrigger.MOUSE
            self.section2_input_trigger.setText('Clique do mouse')
            self.section2_input_trigger.setEnabled(False)
            self.section2_type_action.setEnabled(True)
        
        elif index == TypeTrigger.KEY.name:
            self.type_trigger = TypeTrigger.KEY
            self.section2_input_trigger.setText('Tecla F1')
            self.section2_input_trigger.setEnabled(False)
            self.section2_type_action.setEnabled(True)
        
        elif index == TypeTrigger.TIME.name:
            self.type_trigger = TypeTrigger.TIME
            self.section2_input_trigger.setPlaceholderText('Definir tempo')
            self.section2_input_trigger.setText('')
            self.section2_input_trigger.setEnabled(True)
            self.section2_type_action.setEnabled(False)

    # Active do Input Action
    def active_action(self, index): 
        index = self.section2_type_action.itemData(index)
        self.type_action = None

        if index == TypeAction.CLICK.name: 
            self.type_action = TypeAction.CLICK
            self.section2_input_action.setEnabled(True)
            self.section2_input_action.mousePressEvent = self.input_action()

        elif index == TypeAction.COMAND.name:
            self.type_action = TypeAction.COMAND
            pass 
        elif index == TypeAction.LIST.name:
            self.type_action = TypeAction.LIST
            pass 
        elif index == TypeAction.OS.name:
            self.type_action = TypeAction.OS
            pass 
        elif index == TypeAction.PROGRAM.name:
            self.type_action = TypeAction.PROGRAM
            pass 
        elif index == TypeAction.WRITE.name:
            self.type_action = TypeAction.WRITE
            pass 

    # Ação do Input Action
    def input_action(self):
        def mousePressEvent(event): 
            if event.button() == Qt.LeftButton:
                if self.type_action == TypeAction.CLICK: 
                    pass
                elif self.type_action == TypeAction.CLICK:
                    pass    

        return mousePressEvent

    # Ação do Input Trigger
    def input_trigger(self): 
        self.windows_screen = []

        def mousePressEvent(event): 
            if event.button() == Qt.LeftButton:
                if self.type_trigger == TypeTrigger.IMAGE:
                    from app import app
                    self.hide()
                    self.home.hide()
                    for screen in app.screens():
                        screen_geometry = screen.geometry()
                        window = SelectionPrint(screen_geometry, parent=self, home = self.home)
                        self.windows_screen.append(window)
                    for window in self.windows_screen:
                        window.set_windows(self.windows_screen)
                        window.show()

        return mousePressEvent
    
    # Definir texto do Input Trigger
    def set_text_input_trigger_active_type_action(self, text): 
        self.section2_input_trigger.setText(text)
        self.section2_type_action.setEnabled(True)
