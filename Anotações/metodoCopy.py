carro = {'marca':'Ferrari', 'motor':'v8', 'ano':2020}

#metodo copy()

copia_carro = carro.copy() #O comando copy cria uma copia do objeto.

copia2 = carro #O copia2 vai receber o objeto, assim tendo o mesmo valor.

#metodo fromkeys()

#o metodo dict.fromkeys monta um dicionario com as informacoes obtidas a partir dos parametros lista e valor. 
lista_chaves = ['chave1', 'chave2', 'chave3']
valor = 0

dicio = dict.fromkeys(lista_chaves, valor)

        #Outro exemplo

lista = ['Pedro', '25', '123', '321', 'abcde', '123', '83849']
d = {'a1':lista}

        #Outro exemplo
def teste(a, b, c):
    print(f'a:{a} | b:{b} | c:{c}')

lista = [1, 'banana', True]

teste(lista[0], lista[1], lista[2])
#Desempacotamento de sequencias, forma mais fácil de desempacotar os indices do exemplo o acima.
teste(*lista)

#---------------------------------------------------------------
def teste1(n, s):
    n = n + 2
    s[0] = s[0] + 1
    return

n1 = 1
lista = [1]
teste1(n1, lista)
print('fim')