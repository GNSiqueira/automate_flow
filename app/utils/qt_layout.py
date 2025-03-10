from qt_core import *

# Criação de layout horizontal
def HLayout(parent = None, margin=0, spacing=0):
    if isinstance(parent, (QVBoxLayout, QHBoxLayout)):
        frame = QFrame(parent)
        layout = QHBoxLayout(frame)
        layout.setContentsMargins(margin, margin, margin, margin)
        layout.setSpacing(spacing)
        return layout, frame
    elif isinstance(parent, (QWidget, QFrame)):
        layout = QHBoxLayout(parent)
        layout.setContentsMargins(margin, margin, margin, margin)
        layout.setSpacing(spacing)
        return layout
    else: 
        layout = QHBoxLayout()
        layout.setContentsMargins(margin, margin, margin, margin)
        layout.setSpacing(spacing)
        return layout
    
# Criação de layout vertical
def VLayout(parent = None, margin=0, spacing=0):
    if isinstance(parent, (QVBoxLayout, QHBoxLayout)):
        frame = QFrame(parent)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(margin, margin, margin, margin)
        layout.setSpacing(spacing)
        return layout, frame
    elif isinstance(parent, (QWidget, QFrame)):
        layout = QVBoxLayout(parent)
        layout.setContentsMargins(margin, margin, margin, margin)
        layout.setSpacing(spacing)
        return layout
    else: 
        layout = QVBoxLayout()
        layout.setContentsMargins(margin, margin, margin, margin)
        layout.setSpacing(spacing)
        return layout
    