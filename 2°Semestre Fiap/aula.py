import time

def medir_tempo(limite):
    inicio = time.time()
    for i in range(limite):
        print(f'i: {i}')
        fim = time.time()
    print(f'Tempo: {fim-inicio}')

medir_tempo(100000000)