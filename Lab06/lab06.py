# Sua tarefa será ler as medidas de tempo de um grupo de caracóis e indicar (i)
# quantos animais estão em cada um dos níveis definidos, (ii) qual foi o tempo
# médio para a realização do percurso, (iii) qual foi a maior velocidade e (iv)
# qual foi a menor velocidade. Os valores de velocidade deverão ser expressos
# em cm/min.

# Descrição da entrada
# A entrada será composta por uma ou mais linhas contendo cada uma delas uma
# medida de tempo em segundos. O valor -1 indicará o final da entrada.
# Veja o exemplo:

# 320
# 158
# 400
# 175
# 205
# -1

# Descrição da saída
# A saída será composta por seis linhas que serão descritas a seguir. Note que
# os dados serão precedidos por strings explicativas, escritas propositalmente
# sem acentos. O tempo médio e os valores de velocidade devem ser formatados
# com uma casa decimal. Você pode conferir dicas sobre este tipo de formatação
# no enunciado da Tarefa de Laboratório 02 e na página Formatação em Python.
# Relembramos que as velocidades, em cm/min, devem ser calculadas
# considerando-se o percurso de 33 cm.
#
# Caracois no nivel 0: 2
# Caracois no nivel 1: 1
# Caracois no nivel 2: 2
# Tempo medio: 251.6 s
# Velocidade maxima: 12.5 cm/min
# Velocidade minima: 5.0 cm/min


tempo = int(input())
nivel0 = 0
nivel1 = 0
nivel2 = 0
soma_tempo = 0
tempo_medio = 0
quantidade_caracol = 0
velocidade_maxima = -1
velocidade_minima = -1


def classifica_nivel(tempo_caracol):
    if tempo_caracol < 180:
        return 0
    if 180 <= tempo_caracol < 240:
        return 1
    return 2


def calcula_velocidade(tempo_caracol):
    return 33 / (tempo_caracol / 60)


while tempo != -1:
    nivel = classifica_nivel(tempo)
    velocidade_atual = calcula_velocidade(tempo)
    if velocidade_maxima < velocidade_atual or velocidade_maxima == -1:
        velocidade_maxima = velocidade_atual
    if velocidade_minima > velocidade_atual or velocidade_minima == -1:
        velocidade_minima = velocidade_atual

    soma_tempo += tempo
    quantidade_caracol += 1

    if nivel == 0:
        nivel0 += 1
    elif nivel == 1:
        nivel1 += 1
    else:
        nivel2 += 1

    tempo = int(input())


tempo_medio = soma_tempo / quantidade_caracol

print('Caracois no nivel 0:', nivel0)
print('Caracois no nivel 1:', nivel1)
print('Caracois no nivel 2:', nivel2)
print('Tempo medio: {:.1f} s'.format(tempo_medio))
print('Velocidade maxima: {:.1f} cm/min'.format(velocidade_maxima))
print('Velocidade minima: {:.1f} cm/min'.format(velocidade_minima))
