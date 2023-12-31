import random
import time
import json
import CriandoListas

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def selection_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i+1, len(seq)):
            
            if seq[j] < seq[min_index]:
                
                seq[j], seq[min_index] = seq[min_index], seq[j]

def insertion_sort(lista):
    for i in range (1, len(lista)):
        pivo = lista[i]
        j=i-1
        while ((j >= 0) and (pivo < lista [j])):
            lista[j+1] = lista[j]
            j-=1
            lista[j+1] = pivo

def merge_sort(lista):
    if len(lista)>1:
        
        meio = len(lista) // 2   

        esquerda = lista[:meio]     
        direita = lista[meio:]      

       
        merge_sort(esquerda)        
        merge_sort(direita)   

        i = j = k = 0
        while i < len(esquerda) and j<len(direita):
            if esquerda[i]<direita[j]:
                lista[k]=esquerda[i]
                i+=1
            else:
                lista[k] = direita[j]
                j+=1
            k+=1

        while(i<len(esquerda)):
            lista[k] = esquerda[i]
            i+=1
            k+=1

        while(j<len(direita)):
            lista[k] = direita[j]
            j+=1
            k+=1

def get_time(ordenar, lista):    
    inicio = time.time()    
    metodo_ordenacao(ordenar, lista) 
    fim = time.time()
    return fim - inicio

def metodo_ordenacao(metodo, lista):
    if metodo == 1:
        print("Utilizando Bubble Sort...")
        bubble_sort(lista)
    elif metodo == 2:
        print("Utilizando Selection Sort...")
        selection_sort(lista)
    elif metodo == 3:
        print("Utilizando Insertion Sort...")
        insertion_sort(lista)
    elif metodo == 4:
        print("Utilizando Merge Sort...")
        merge_sort(lista)
    else:
        print("Opção inválida. Tente novamente.")

def menuPrincipal():
    while True:
        print("*== Teste de ordenação de listas ==*")
        print("Escolha um dos algoritmos abaixo")
        print("===========================")
        print("1. \033[32mBubble Sort\033[0m")
        print("===========================")
        print("2. \033[32mSelection Sort\033[0m")
        print("===========================")
        print("3. \033[32mInsertion Sort\033[0m")
        print("===========================")
        print("4. \033[32mMerge Sort\033[0m")
        print("===========================")
        print("5. \033[32mSair do programa\033[0m")
        print("===========================")

        ordenar = int(input("Digite o número da opção de ordenação desejada: "))

        if ordenar == 5:
            print("Saiu do programa")
            break
        print("Tamanhos disponiveis: 10000, 100000, 500000, 1000000, 5000000")
        tamanho = int(input("Digite o tamanho da lista que deseja ordenar: "))
        nome_arquivo = f'./CPS/CP5/Listas/Lista_{tamanho}.json'

        with open(nome_arquivo, 'r') as arquivo:
            lista_desordenada = json.load(arquivo)

        print(f"\nOrdenando lista de \033[32m{tamanho}\033[0m elementos. Vai dormir e deixa rodando...")
        tempo = get_time(ordenar, lista_desordenada)
        print(f"Tempo de execução: \033[32m{tempo:.3f}\033[0m segundos")
        print(f"Algoritmo: \033[32m{get_nome_algoritmo(ordenar)}\033[0m")

        # Mostra a lista ordenada
        #print("Lista ordenada:")
        #print(lista_desordenada)

def get_nome_algoritmo(metodo):
    if metodo == 1:
        return "Bubble Sort"
    elif metodo == 2:
        return "Selection Sort"
    elif metodo == 3:
        return "Insertion Sort"
    elif metodo == 4:
        return "Merge Sort"
    else:
        return "Opção inválida"

#Programa Principal
menuPrincipal()



