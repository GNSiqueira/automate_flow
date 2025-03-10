import pyautogui
import keyboard

def on_click():
    # Captura a posição do mouse
    x, y = pyautogui.position()
    print(f"Posição do mouse: ({x}, {y})")

print("Aguardando cliques do mouse... Pressione Ctrl+C para interromper.")

try:
    while True:
        # Verifica se o botão esquerdo do mouse foi clicado
        if keyboard.is_pressed('left mouse'):
            on_click()
            # Adiciona um pequeno atraso para evitar múltiplas detecções
            keyboard.wait('left mouse', suppress=False)
except KeyboardInterrupt:
    print("Monitoramento interrompido.")
