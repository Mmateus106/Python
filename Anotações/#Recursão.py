#Recursão

#Exemplo1 - somar uma lista de numeros (sem recursao)
#(1, 3, 5, 7, 9) = 25

def somarNumeros(lista):
    soma = 0
    for i in lista:
        soma+=i
    return soma
    
#programa pricipal
lista = [1, 3, 5, 7, 9]
print(f"soma: {somarNumeros(lista)}")

#======================================
#((((1+3) + 5) + 7) + 9)
#ordem inversa
# (1 + (3 + (5 + (7 + 9))))
# (1 + (3 + (5 + 16)))
# (1 + (3 + 21))
# (1 + 24)
#total = 25

#Função Recursiva
# somar o primeiro elemento da lista[0],
# com os demais numeros da lista[1:]

def somarRecursivo(lista):
    if len(lista) == 1:
        return lista[0]
    else: 
        return lista[0] + somarRecursivo(lista[1:])
    
#Teste
print(f'soma: {somarRecursivo(lista)}')

#As tres leis da recursao
#1) Um algoritmo recursivo deve ter um caso basico
#2) Um algoritmo recursivo deve mudar de estado e se
#aproximar do caso basico
#3) Um algoritmo recursivo deve chamar a si mesmo, recursivamente
