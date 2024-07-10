import json
import random

def criar_lista_num(tamanho):
    return [random.randint(1, 10000) for _ in range(tamanho)]

def salvar_json(nome_arquivo, lista):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(lista, arquivo)

def criar_salvar_json(tamanho):
    lista = criar_lista_num(tamanho)
    nome_arquivo = f'./CPS/CP5/Listas/Lista_{tamanho}.json'
    salvar_json(nome_arquivo, lista)
    print(f'Arquivo {nome_arquivo} com lista desordenada gerada!')

tamanhos = [10000, 100000, 500000, 1000000, 5000000]
for tamanho in tamanhos:
    criar_salvar_json(tamanho)
