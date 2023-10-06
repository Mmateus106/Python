def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

#Programa principal
lista = [3, 7, 9, 1, 2, 4, 5, 6, 8]
print(f"Lista desordenada: {lista}")
bubble_sort(lista)
print(f"Lista ordenada: {lista}")