import os, json

arquivo = ['teste', 'teste2', 'teste3']
path = './config.json'


def arquivo_w(path, arquivo):
    with open(path, 'w') as f:
        json.dump(arquivo, f, indent=2)

def arquivo_r(path):
    with open(path, 'r') as f:
        config = json.load(f)
    return config

