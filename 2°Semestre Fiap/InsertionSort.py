# Algoritmo Insertion Sort - ordenação por inserção
# https://www.youtube.com/watch?v=EdIKIf9mHk0   <-- Link de video demonstrativo sobre Insertion Sort

def insertion_sort(lista):
    for i in range (1, len(lista)):
        pivo = lista[i]
        j=i-1
        while ((j >= 0) and (pivo < lista [j])):
            lista[j+1] = lista[j]
            j-=1
            lista[j+1] = pivo

#Programa Principal
lista = [12, 11, 13, 5, 6]
print(f'Lista Original: {lista}')
insertion_sort(lista) #chamada do algoritmo de ordenação
print(f'Lista Ordenada: {lista}')