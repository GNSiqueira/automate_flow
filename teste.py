from pynput import keyboard
import json

FILE_NAME = "atalhos.json"

def load_shortcuts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_shortcut(shortcut):
    shortcuts = load_shortcuts()
    if shortcut not in shortcuts:
        shortcuts.append(shortcut)
        with open(FILE_NAME, "w") as file:
            json.dump(shortcuts, file, indent=4)
        print(f"Atalho salvo: {shortcut}")

current_keys = set()

def on_press(key):
    try:
        current_keys.add(key.char)
    except AttributeError:
        current_keys.add(str(key))

    shortcut = "+".join(sorted(current_keys))
    save_shortcut(shortcut)

def on_release(key):
    try:
        current_keys.remove(key.char)
    except AttributeError:
        current_keys.remove(str(key))

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Pressione atalhos de teclado para salvar (CTRL + C para sair)...")
    print
