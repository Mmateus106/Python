# CP1 Segundo semestre / Computational Thinking Using Python
# André Rohreggeer Machado RM98110
# Mateus Mantovani Araújo RM98524

import random

# Função para inicializar o tabuleiro
def inicializarTabuleiro():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    return tabuleiro

# Função para imprimir o tabuleiro
def imprimirTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-----")

# Função para verificar se a posição é válida
def posicaoValida(tabuleiro, linha, coluna):
    if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' ':
        return True
    return False

# Função para verificar se há um vencedor
def verificaVencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(cell == jogador for cell in linha):
            return True

    # Verificar colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False
# Função para verificar se o jogo empatou
def verificaVelha(tabuleiro):
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

# Função para a jogada da máquina (nível fácil)
def jogadaMaquinaFacil(tabuleiro):
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if posicaoValida(tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = 'O'
            break

# Função para o modo jogador contra jogador
def modoJogador():
    tabuleiro = inicializarTabuleiro()
    jogador1 = input("Jogador 1, escolha X ou O: ").upper()
    jogador2 = 'X' if jogador1 == 'O' else 'O'
    vez_do_jogador1 = True
    pontos_jogador1 = 0
    pontos_jogador2 = 0

    while True:
        imprimirTabuleiro(tabuleiro)
        jogador_atual = jogador1 if vez_do_jogador1 else jogador2
        print(f'Vez do Jogador {jogador_atual}')

        linha = int(input('Informe a linha: '))
        coluna = int(input('Informe a coluna: '))

        if not posicaoValida(tabuleiro, linha, coluna):
            print('Jogada inválida. Tente novamente.')
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificaVencedor(tabuleiro, jogador_atual):
            imprimirTabuleiro(tabuleiro)
            print(f'Jogador {jogador_atual} venceu!')
            if jogador_atual == jogador1:
                pontos_jogador1 += 1
            else:
                pontos_jogador2 += 1
            print(f'Pontos: Jogador 1 ({pontos_jogador1}) - Jogador 2 ({pontos_jogador2})')
            
            # Verificar se algum jogador acumulou 3 pontos
            if pontos_jogador1 >= 3:
                print("Jogador 1 venceu a partida!")
                break
            elif pontos_jogador2 >= 3:
                print("Jogador 2 venceu a partida!")
                break
                
            tabuleiro = inicializarTabuleiro()  # Reiniciar o tabuleiro
        elif verificaVelha(tabuleiro):
            imprimirTabuleiro(tabuleiro)
            print('O jogo empatou!')
            tabuleiro = inicializarTabuleiro()  # Reiniciar o tabuleiro
            
        vez_do_jogador1 = not vez_do_jogador1

# Função para o modo jogador contra máquina (nível fácil)
def modoFacil():
    tabuleiro = inicializarTabuleiro()
    jogador1 = input("Jogador, escolha X ou O: ").upper()
    jogador2 = 'X' if jogador1 == 'O' else 'O'
    vez_do_jogador1 = True
    pontos_jogador1 = 0
    pontos_jogador2 = 0

    while True:
        imprimirTabuleiro(tabuleiro)
        jogador_atual = jogador1 if vez_do_jogador1 else jogador2
        print(f'Vez do Jogador {jogador_atual}')

        if vez_do_jogador1:
            linha = int(input('Informe a linha: '))
            coluna = int(input('Informe a coluna: '))
            if not posicaoValida(tabuleiro, linha, coluna):
                print('Jogada inválida. Tente novamente.')
                continue
            tabuleiro[linha][coluna] = jogador_atual
        else:
            jogadaMaquinaFacil(tabuleiro)

        if verificaVencedor(tabuleiro, jogador_atual):
            imprimirTabuleiro(tabuleiro)
            if jogador_atual == jogador1:
                print('*--* Você venceua partida! *--*')
                pontos_jogador1 += 1
            else:
                print('*--* A máquina venceu! *--*')
                pontos_jogador2 += 1
            print(f'Pontos: Jogador ({pontos_jogador1}) - Máquina ({pontos_jogador2})')

            # Verificar se algum jogador acumulou 3 pontos
            if pontos_jogador1 >= 3:
                print("*--* Jogador venceu a rodada! *--*")
                break
            elif pontos_jogador2 >= 3:
                print("*--* Máquina venceu a rodada! *--*")
                break
                
            tabuleiro = inicializarTabuleiro()  # Reiniciar o tabuleiro
        elif verificaVelha(tabuleiro):
            imprimirTabuleiro(tabuleiro)
            print('*--* O jogo empatou! *--*')
            tabuleiro = inicializarTabuleiro()  # Reiniciar o tabuleiro
            
        vez_do_jogador1 = not vez_do_jogador1

# Função para o menu principal
def menuPrincipal():
    print("*-- BEM-VINDO AO JOGO DA VELHA --*!")
    print("Escolha uma opção:")
    print("--------------------------------")
    print("1. Jogador vs. Jogador")
    print("--------------------------------")
    print("2. Jogador vs. Robô (Modo Fácil)")
    print("--------------------------------")
    print("3. Sair")
    print("--------------------------------")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        modoJogador()
    elif opcao == "2":
        modoFacil()
    elif opcao == "3":
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menuPrincipal()

# Função principal do jogo
def jogoDaVelha():
    while True:
        menuPrincipal()

if __name__ == "__main__":
    jogoDaVelha()