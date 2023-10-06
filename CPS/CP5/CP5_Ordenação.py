import random
import time


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
            #seleciona o menor elemento em cada iteração
            if seq[j] < seq[min_index]:
                #troca os elementos - atribuição paralela
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
        #i - controle da lista esquerda 
        #j - controle da lista direita
        #k - controle da lista anterior à recursão
        #Verificação dos elementos da lista esquerda
        while(i<len(esquerda)):
            lista[k] = esquerda[i]
            i+=1
            k+=1

        #Verificação dos elementos da lista direita
        while(j<len(direita)):
            lista[k] = direita[j]
            j+=1
            k+=1

# Função para o menu principal
def menuPrincipal():
    print("*-- Teste de ordenação --*!")
    print("Escolha uma opção:")
    print("--------------------------------")
    print("1. Bubble Sort")
    print("--------------------------------")
    print("2. Selection Sort")
    print("--------------------------------")
    print("3. Insertion Sort")
    print("--------------------------------")
    print("4. Merge Sort")
    print("--------------------------------")
    print("5. Sair do programa")
    print("--------------------------------")

    ordenar = input("Digite o número da opção de ordenação desejada: ")

    if ordenar == "1":
        bubble_sort()
    elif ordenar == "2":
        selection_sort()
    elif ordenar == "3":
        insertion_sort()
    elif ordenar == "4":
        merge_sort()
    elif ordenar =="5":
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menuPrincipal()

#Programa Principal