from app.utils.qt_layout import *
from qt_core import *
from app.views.ui import Ui
from app.views.interfaces.ui_new_stream_modal import Modal_New_Stream
from app.utils.enums import Layout, Alignment
from app.utils.qt_table import *

class Home(Ui): 
    def __init__(self):
        super().__init__(layout=Layout.HORIZONTAL, larg=800, alt=500)

        self.section1 = VLayout(margin=20, spacing=10)
        
        self.section1_table = QTableWidget(2, 2)
        self.section1_table.setHorizontalHeaderLabels(['Selecionar', 'Fluxo'])

        expanding_header_table(self.section1_table, 1, expanding=True)
        expanding_header_table(self.section1_table, 0, expanding=False)

        self.section1_top_table = HLayout(spacing=10)

        self.section1_top_table_button_new = QPushButton("Novo Fluxo +")
        self.section1_top_table_button_new.clicked.connect(self.open_new_stream_modal)
        self.section1_top_table_search_streams = QLineEdit(placeholderText="Procurar fluxo...")

        self.section1_top_table.addWidget(self.section1_top_table_button_new)
        self.section1_top_table.addWidget(self.section1_top_table_search_streams)

        self.section1.addLayout(self.section1_top_table)
        self.section1.addWidget(self.section1_table)

        self.section2 = VLayout(margin=20, spacing=10)
        self.section2.setAlignment(Alignment.Center.value)

        self.section2_button_edit_stream = QPushButton("Editar fluxo ")
        self.section2_button_edit_stream.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.section2_button_delete_stream = QPushButton("Deletar Fluxo  X")
        self.section2_button_start_stream = QPushButton("Start Fluxo  ▶")

        self.section2.addWidget(self.section2_button_edit_stream)
        self.section2.addWidget(self.section2_button_delete_stream)
        self.section2.addWidget( self.section2_button_start_stream)

        self.setup(self.section1, expanding=2)
        self.setup(self.section2, expanding=1)
    
    def open_new_stream_modal(self):
         modal = Modal_New_Stream(self)
         modal.show()