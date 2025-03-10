import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPainter, QPixmap
from PySide6.QtWidgets import QApplication
import numpy as np

def capture_all_screens():
    app = QApplication(sys.argv)
    
    # Pega todas as telas conectadas
    screens = app.screens()
    
    # Lista para armazenar as imagens de cada tela
    screen_images = []
    
    # Captura a imagem de cada tela
    for screen in screens:
        pixmap = screen.grabWindow(0)  # Captura a tela inteira
        screen_images.append(pixmap)
    
    # Obter as dimensões totais da imagem combinada
    total_width = sum(pixmap.width() for pixmap in screen_images)
    max_height = max(pixmap.height() for pixmap in screen_images)
    
    # Criar uma imagem em branco para colocar todas as imagens juntas
    final_image = QImage(total_width, max_height, QImage.Format_RGB888)
    final_image.fill(Qt.white)
    
    # Usar um QPainter para desenhar cada imagem na imagem final
    painter = QPainter(final_image)
    x_offset = 0
    
    for pixmap in screen_images:
        painter.drawPixmap(x_offset, 0, pixmap)
        x_offset += pixmap.width()
    
    painter.end()
    
    # Salvar a imagem final em um arquivo
    final_image.save("screenshot_all_screens.png")
    print("Screenshot salva como 'screenshot_all_screens.png'")

if __name__ == "__main__":
    capture_all_screens()
