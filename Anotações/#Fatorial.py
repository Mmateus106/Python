#Fatorial de n
#n!
# n = 4
# 4! = 4*3*2*1 = 24
# 5! = 5*4*3*2*1 = 120
# 6! = 6*5*4*3*2*1 = 720

# Aplicacao em python

def fatorial(n):
    if(n==0):
        return 1
    elif n == 1: #caso basico
        return 1
    else:
        return n * fatorial(n-1) #chamada recursiva
    
    
#Principal
while True: 
    n = int(input('Numero: '))
    if n==0:
        break
    print(f"Fatorial de {n}: {fatorial(n)}")
