from enum import Enum
from qt_core import *

class Layout(Enum):
        VERTICAL = "V"
        HORIZONTAL = "H"


class TypeTrigger(Enum):
        IMAGE = "Imagem"
        KEY = "Tecla"
        TIME = "Tempo"
        MOUSE = "Clique do mouse"

class TypeAction(Enum):
        OS = "Comandos do sistema"
        CLICK = "Click do mouse"
        WRITE = "Escrever"
        COMAND = "Comando de teclado"
        LIST = "Lista"

class Alignment(Enum):
        Top = Qt.AlignmentFlag.AlignTop
        Bottom = Qt.AlignmentFlag.AlignBottom
        Left = Qt.AlignmentFlag.AlignLeft
        Right = Qt.AlignmentFlag.AlignRight
        Center = Qt.AlignmentFlag.AlignCenter
