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

def get_time(ordenar):    
    inicio = time.time()    
    time.sleep(ordenar) # <- Chamar a função de ordenação aq
    fim = time.time()
    return fim-inicio

def medir_tempo(limite):
    inicio = time.time()
    for i in range(limite):
        print(f'i: {i}')
        fim = time.time()
    print(f"Tempo: {fim-inicio}")

def testar_metodo_ordenacao(metodo, lista):
    if metodo == 1:
        print("Usando Bubble Sort")
        bubble_sort(lista)
    elif metodo == 2:
        print("Usando Selection Sort")
        selection_sort(lista)
    elif metodo == 3:
        print("Usando Insertion Sort")
        insertion_sort(lista)
    elif metodo == 4:
        print("Usando Merge Sort")
        merge_sort(lista)
    else:
        print("Opção inválida. Tente novamente.")

def menuPrincipal():
    while True:
        print("*-- Teste de ordenação de listas --*!")
        print("Escolha uma opção:")
        print("---------------------------")
        print("1. Bubble Sort")
        print("---------------------------")
        print("2. Selection Sort")
        print("---------------------------")
        print("3. Insertion Sort")
        print("---------------------------")
        print("4. Merge Sort")
        print("---------------------------")
        print("5. Sair do programa")
        print("---------------------------")

        ordenar = int(input("Digite o número da opção de ordenação desejada: "))

        if ordenar == 5:
            print("Saiu do programa")
            break

menuPrincipal()


