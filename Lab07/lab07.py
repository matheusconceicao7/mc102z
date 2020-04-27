tipo_objeto = input()
caractere = input()
dimensao = int(input())


def desenha_quadrado(caractere, dimensao):
    for n_linha in range(dimensao):
        print(caractere * dimensao)


def desenha_triangulo(caractere, dimensao):
    for n_linha in range(1, dimensao+1, 1):
        qtd_caracteres = n_linha * 2 - 1
        linha = (caractere * qtd_caracteres).center(int((dimensao * 2)))
        print(linha.rstrip())


def desenha_losango(caractere, dimensao):
    desenha_triangulo(caractere, dimensao)
    linha_abaixo_do_meio = dimensao * 2 - 3
    for q in range(linha_abaixo_do_meio, 0, -2):
        linha = (caractere * q).center(int(dimensao * 2))
        print(linha.rstrip())


def desenha_hexagono(caractere, dimensao):
    n_linhas = dimensao * 2 - 1
    largura_max = 3 * dimensao - 2
    for n_linha in range(0, dimensao, 1):
        qtd_caracteres = dimensao + ((n_linha * 2))
        linha = (caractere * qtd_caracteres).center(largura_max)
        print(linha.rstrip())
    for q in range(largura_max - 2, dimensao-1, -2):
        linha = (caractere * q).center(largura_max)
        print(linha.rstrip())


def desenha_octogono(caractere, dimensao):
    largura_max = 3 * dimensao - 2
    for i in range(dimensao - 1):
        linha = (caractere * (dimensao + 2*i)).center(largura_max)
        print(linha.rstrip())
    for i in range(dimensao):
        linha = (caractere * largura_max).center(largura_max)
        print(linha.rstrip())
    for i in range(largura_max - 2, dimensao-1, -2):
        linha = (caractere * i).center(largura_max)
        print(linha.rstrip())


if tipo_objeto == "Q":
    desenha_quadrado(caractere, dimensao)
elif tipo_objeto == "T":
    desenha_triangulo(caractere, dimensao)
elif tipo_objeto == "L":
    desenha_losango(caractere, dimensao)
elif tipo_objeto == "H":
    desenha_hexagono(caractere, dimensao)
elif tipo_objeto == "O":
    desenha_octogono(caractere, dimensao)
else:
    print("Identificador invalido.")
if dimensao < 3:
    print("Dimensao invalida.")
