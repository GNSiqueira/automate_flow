import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageGrab

def carregar_imagem(imagem):
    """Carrega uma imagem no formato adequado para o OpenCV (convertendo para escala de cinza)."""
    imagem_cv = np.array(imagem)  # Converte a imagem PIL para um array NumPy
    imagem_cv = cv2.cvtColor(imagem_cv, cv2.COLOR_RGB2GRAY)  # Converte para escala de cinza
    return imagem_cv

def localizar_imagem(template, confianca=0.8):
    resultado = cv2.matchTemplate(tela_imagem(), carregar_imagem(Image.open(template)), cv2.TM_CCOEFF_NORMED)
    locais = np.where(resultado >= confianca)
    posicoes = list(zip(*locais[::-1]))

    if posicoes:
        return posicoes
    else:
        return False

def tela_imagem():
        # Captura a tela inteira
    screenshot = ImageGrab.grab()
    # Carregar a imagem da tela para processamento com OpenCV
    imagem = carregar_imagem(screenshot)

    return imagem

