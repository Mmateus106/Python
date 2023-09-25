#Merge Sort - Ordenação por intercalação (mistura)
#Complexidade: O(n*log(n))

def merge_sort(lista):
    if len(lista)>1:
        
        #Encontrando o meio da lista
        meio = len(lista) // 2      #parte inteira da lista

        #Dividindo a lista em duas (fatiamento de listas)
        esquerda = lista[:meio]     #Esquerdo do meio até a metade
        direita = lista[meio:]      #Direito do meio para frente

        #Chamada recursiva
        merge_sort(esquerda)        #Ordena as sub-listas
        merge_sort(direita)   

        #Variáveis de controle
        #i - fará o controle da lista esquerda 
        #j - fará o controle da lista direita
        #k - fará o controle da lista anterior à recursão
        i = j = k = 0
        while i < len(esquerda) and j<len(direita):
            if esquerda[i]<direita[j]:
                lista[k]=esquerda[i]
                i+=1
            else:
                lista[k] = direita[j]
                j+=1
            k+=1
        
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

#Programa principal
lista = [12, 11, 13, 5, 6, 7]
print(f'Lista Original: {lista}')
merge_sort(lista)   #chama função MergeSort()
print(f'Lista Ordenada: {lista}')
