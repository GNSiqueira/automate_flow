import keyboard
import time

# Função para simular a digitação com intervalo
def digitar_com_delay(texto, intervalo=0.1):
    keyboard.write(texto, delay=intervalo)  # Digita o texto com o intervalo definido
    print(f"Texto digitado: {texto}")

# Exemplo de uso
print("Iniciando a digitação...")
digitar_com_delay("Olá, esta é uma digitação simulada!", intervalo=0.2)  # Intervalo de 0.2 segundos entre cada caractere
