from PySide6.QtCore import Qt, QEvent, QObject
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout

class EventFilter(QObject):
    def __init__(self):
        super().__init__()

    def eventFilter(self, obj, event):
        """
        Sobrescreva o método eventFilter para capturar os eventos.
        """
        if isinstance(obj, QLineEdit):
            if event.type() == QEvent.MouseButtonPress:
                print("Clique detectado no QLineEdit!")
                return True  # Evento tratado

            if event.type() == QEvent.KeyPress:
                print(f"Tecla pressionada no QLineEdit: {event.key()}")
                return True  # Evento tratado

        elif isinstance(obj, QPushButton):
            if event.type() == QEvent.MouseButtonPress:
                print("Clique detectado no QPushButton!")
                return True  # Evento tratado

        return super().eventFilter(obj, event)  # Deixa o evento passar

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Event Filter Example")
        self.setGeometry(100, 100, 400, 300)

        # Criando dois widgets diferentes
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Clique aqui ou pressione uma tecla!")

        self.button = QPushButton("Clique no botão!", self)

        # Criando e registrando o filtro de eventos
        self.event_filter = EventFilter()
        self.line_edit.installEventFilter(self.event_filter)  # Filtro para QLineEdit
        self.button.installEventFilter(self.event_filter)     # Filtro para QPushButton

        # Layout para adicionar os widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

if __name__ == "__main__":
    app = QApplication([])

    # Criar e exibir o widget
    widget = MyWidget()
    widget.show()

    app.exec()
