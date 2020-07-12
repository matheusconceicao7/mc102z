"""
lista = 1 2 3 4 5

output:
.......
.    |.
.   ||.
.  |||.
. ||||.
.|||||.
.......

"""

def desenha_lista(lista):
    altura_maxima = max(lista)
    print((len(lista)+2)*'.')
    for i in range(altura_maxima, 0, -1):
        print(".", end="")
        for j in range(len(lista)):
            if(lista[j] >= i):
                print("|", end="")
            else:
                print(" ", end="")
        print(".")
    print((len(lista)+2)*'.')

def ordenacao_bolha(lista):
    desenha_lista(lista)
    for i in range(len(lista) - 1, 0, -1):
        for j in range(i):
            if(lista[j] > lista[j+1]):
                lista[j],lista[j+1] = lista[j+1],lista[j]
                desenha_lista(lista)


lista = [int(i) for i in input().split()]

ordenacao_bolha(lista)
