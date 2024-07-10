# s = [('pt', 'arroz'), ('en', 'rice'), ('fr', 'riz')]

# t1 = [1, 2, 3]
# t2 = [3, 4, 5]
# t3 = [7, 8, 9]
# t4 = [t1, t2, t3]

# t1[1] #Te direciona para a posição 1 da lista t1
# t4[2][2] #Te direciona na posição 2 da lista t4(t3), e depois te direciona para a posição 2 dentro da lista t3

#-----------------------------------------------------------------

#Tabela

# produtos = [['smartphone', '100', '1999.00', True],
#             ['tv', 5, 2500.00, False],
#             ['notebook', 2, 3000.00, True]]
# print(produtos)

#-------------------------------------------------------------------
#Exemplos
# alunos = [[7, 2, 9],
#          [4, 5, 8],
#          [9, 6, 4],
#          [10, 5, 8]]

# def calcula_media(aluno):
#     soma=0
#     for nota in aluno:
#         soma+=nota
#     return soma/len(aluno)

# def obter_medias(alunos):
#     medias = []
#     for aluno in alunos:
#         media = calcula_media(aluno)
#         medias.append(media)
# #Principal

# lista_medias = obter_medias(alunos)

#--------------------------------------------------------------
def coleta_notas():
    notas = input().split()
    for i in range(len(notas)):
        notas[i] = float(notas[i])
    return notas

def preenche_turma(qtde_alunos):
    turma = []
    for i in range(qtde_alunos):
        print(f'{i} + {1}° aluno: ', end=' ')
        aluno = coleta_notas()
        turma.append(aluno)
    return turma

def calcula_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
    return soma / len(aluno)

def resumo_turma(turma):
    for aluno in turma:
        media = calcula_media(aluno)
        print(f'notas: {aluno} | média: {media:2.2f}')
#Principal

qtde_alunos = int(input('Quantidade: '))
turma = preenche_turma(qtde_alunos)
resumo_turma(turma)


            
