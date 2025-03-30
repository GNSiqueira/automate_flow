from pyautogui import click, hotkey
from time import sleep, time
import shutil, os
from pynput import keyboard
from pynput.keyboard import Controller
from pynput.mouse import Listener, Button
from app.utils.configs import Configs
from app.utils.locate_image import localizar_imagem

def Trigger(type_trigger, trigger):
    def procurarImagem(img, tempo_max=5):
        inicio = time()

        while time() - inicio < tempo_max:
            if localizar_imagem(img):
                return True

        raise TypeError("Imagem não encontrada")

    def monitorarTecla(tecla="ctrl"):
        def on_press(key):
            if hasattr(key, 'name') and key.name == tecla:
                return False

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

        sleep(1)
        return True

    def monitorarMouse():
        def on_click(x, y, button, pressed):
            if pressed and button == Button.left:
                return False

        with Listener(on_click=on_click) as listener:
            listener.join()

        return True

    def monitorarTempo(temp):
        sleep(float(temp))
        return True

    if type_trigger == 'IMAGE':
        path = Configs.repositoriesImage()
        return procurarImagem(os.path.join(path, trigger))

    elif type_trigger == 'KEY':
        monitorarTecla()

    elif type_trigger == 'TIME':
        monitorarTempo(trigger)

    elif type_trigger == 'MOUSE':
        monitorarMouse()


def Action(type_action, action):
    if type_action == "OS":
        if action[0] == 'Copiar':
            if os.path.isdir(action[1]):
                shutil.copytree(action[1], action[2])
            else:
                shutil.copy(action[1], action[2])

        elif action[0] == 'Mover':
                shutil.move(action[1], action[2])

        elif action[0] == 'Deletar':
            if os.path.isdir(action[1]):
                shutil.rmtree(action[1])

            else:
                os.remove(action[1])

        elif action[0] == 'Criar':
            os.mkdir(os.path.join(action[1], action[2]))

        elif action[0] == 'Adicionar Comando':
            os.system(action[1])

    elif type_action == "CLICK":
        click(action[1], action[2])

    elif type_action == "WRITE":
        # if os.name != 'nt':
        keyboard = Controller()
        for char in str(action[0]):
            keyboard.type(char)
        sleep(0.5)
        return True
        # keyboard.write(text=action[0], )
        # sleep(0.5)
        # return True

    elif type_action == "COMAND":
        c = int(action[1])
        while c > 0:
            hotkey(*action[2:])
            c -= 1
            sleep(0.05)
