from app.utils.qt_layout import *
from app.utils.configs import Configs
from qt_core import *
from app.views.ui import Ui
from app.views.interfaces.ui_new_stream_modal import Modal_New_Stream
from app.utils.enums import Layout, Alignment
from app.utils.qt_table import *
from app.utils.pyautogui_controller import Action, Trigger

class Home(Ui):
    def __init__(self):
        super().__init__(layout=Layout.HORIZONTAL, larg=800, alt=500, FixedSize=True)

        self.section1 = VLayout(margin=20, spacing=10)

        self.section1_table = QTableWidget(0, 1)
        self.section1_table.setHorizontalHeaderLabels(['Fluxo'])
        self.section1_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.section1_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.section1_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.section1_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.section1_table.setStyleSheet("""
            QTableWidget::item:selected {
                background-color: #0c2cab;  /* Cor de fundo azul forte para a linha selecionada */
                color: white;               /* Cor do texto ao selecionar */
            }
        """)

        expanding_header_table(self.section1_table, 0, expanding=True)

        self.section1_top_table = HLayout(spacing=10)

        self.itensToTable()

        self.section1_top_table_button_new = QPushButton("Novo Fluxo +")
        self.section1_top_table_button_new.clicked.connect(self.openNewStreamModal)
        self.section1_top_table_search_streams = QLineEdit(placeholderText="Procurar fluxo...")

        self.section1_top_table.addWidget(self.section1_top_table_button_new)
        self.section1_top_table.addWidget(self.section1_top_table_search_streams)

        self.section1.addLayout(self.section1_top_table)
        self.section1.addWidget(self.section1_table)

        self.section2 = VLayout(margin=20, spacing=10)
        self.section2.setAlignment(Alignment.Center.value)

        self.section2_button_edit_stream = QPushButton("Editar fluxo ")
        self.section2_button_edit_stream.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.section2_button_edit_stream.clicked.connect(self.editar)
        self.section2_button_delete_stream = QPushButton("Deletar Fluxo  X")
        self.section2_button_delete_stream.clicked.connect(self.delete)
        self.section2_button_start_stream = QPushButton("Start Fluxo  ▶")
        self.section2_button_start_stream.clicked.connect(self.start)

        self.section2.addWidget(self.section2_button_edit_stream)
        self.section2.addWidget(self.section2_button_delete_stream)
        self.section2.addWidget( self.section2_button_start_stream)

        self.setup(self.section1, expanding=2)
        self.setup(self.section2, expanding=1)

        self.show()

    def openNewStreamModal(self):
        state_modal = self.state_modal(self)
        state_modal.close()
        self.nova_janela = Modal_New_Stream(state_modal)
        self.nova_janela.atualizar_info.connect(self.itensToTable)
        self.nova_janela.show()

    def itensToTable(self):
        arquivos = Configs.arquivo_leitura()

        self.section1_table.setRowCount(0)

        for num, arquivo in enumerate(arquivos):
            self.section1_table.insertRow(num)
            self.section1_table.setItem(num, 0, QTableWidgetItem(str(arquivo[0])))

        del arquivos

        return True

    def editar(self):
        select = self.section1_table.selectedItems()
        if select:
            state_modal = self.state_modal(self)
            state_modal.close()
            self.nova_janela = Modal_New_Stream(state_modal, int(select[0].row() + 1))
            self.nova_janela.show()

    def start(self):
        select = self.section1_table.selectedItems()
        if select:
            streams = Configs.arquivo_leitura()
            streams = streams[select[0].row()]
            try:
                self.hide()

                for stream in streams[1:]:
                    Trigger(stream['type_trigger'], stream['trigger'])
                    Action(stream['type_action'], stream['action'])

                self.show()
            except:
                QMessageBox.information(None, 'Informação', 'Erro ao executar fluxo!')

    def delete(self):
        select = self.section1_table.selectedItems()
        if select:
            streams = Configs.arquivo_leitura()
            streams.pop(select[0].row())
            Configs.arquivo_escrita(streams)
            self.itensToTable()


    class state_modal:
        def __init__(self, parent):
            self.parent = parent

        def close(self):
            self.parent.close()

        def hide(self):
            self.parent.hide()

        def show(self):
            self.parent.update()
            self.parent.show()
