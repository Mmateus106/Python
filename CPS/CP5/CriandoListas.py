import json
import random

def criar_lista_num(lenght):
    return [random.randint(1, 10000) for _ in range(lenght)]

def salvar_json(nome_arquivo, lista):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(lista, arquivo)

def criar_e_salvar_json(lenght):
    lista = criar_lista_num(lenght)
    nome_arquivo = f'./CPS/CP5/Listas/Lista_{lenght}.json'
    salvar_json(nome_arquivo, lista)
    print(f'Arquivo {nome_arquivo} com lista desordenada gerada!')

tamanhos = [10000, 100000, 500000, 1000000, 5000000]
for lenght in tamanhos:
    criar_e_salvar_json(lenght)
