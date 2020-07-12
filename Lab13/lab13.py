def desenha_lista(lista, marcar_meio, meio, exibir_de, exibir_ate):
    for index,x in enumerate(lista):
        if(index > exibir_ate):
            continue
        if(index < exibir_de):
            print("      ", end="")
        elif(marcar_meio == True and x == meio):
            print("+=====", end="")
        else:
            print("+-----", end="")
    print("+")
    for index,x in enumerate(lista):
        if(index > exibir_ate):
            continue
        if(index < exibir_de):
            print("      ", end="")
        elif(marcar_meio == True and x == meio):
            print("||{}|".format(x), end="")
        else:
            print("| {} ".format(x), end="")
    print("|")
    for index,x in enumerate(lista):
        if(index > exibir_ate):
            continue
        if(index < exibir_de):
            print("      ", end="")
        elif(marcar_meio == True and x == meio):
            print("+=====", end="")
        else:
            print("+-----", end="")
    print("+")

def busca_binaria(lista,elemento):
    posicao_primeiro_elem = 0
    posicao_ultimo_elem =len(lista)-1
    posicao_meio = (posicao_primeiro_elem+posicao_ultimo_elem)//2
    desenha_lista(lista,False,"",posicao_primeiro_elem,posicao_ultimo_elem)
    if(lista != sorted(lista)):
        return -2
    else:
        desenha_lista(lista,True,lista[posicao_meio],posicao_primeiro_elem,posicao_ultimo_elem)
        while(posicao_ultimo_elem >= posicao_primeiro_elem):
            if(lista[posicao_meio] == elemento):
                print("Encontrado na posicao: {}".format(posicao_meio))
                return True
            else:
                if elemento < lista[posicao_meio]:
                    posicao_ultimo_elem = posicao_meio - 1
                else:
                    posicao_primeiro_elem = posicao_meio + 1
            posicao_meio = (posicao_primeiro_elem+posicao_ultimo_elem)//2
            desenha_lista(lista, True, lista[posicao_meio],posicao_primeiro_elem,posicao_ultimo_elem)
            if(posicao_primeiro_elem == posicao_ultimo_elem and lista[posicao_meio] != elemento):
                return False
    return False





elemento = input().zfill(3)
lista = [e.zfill(3) for e in input().split()]

print("Elemento procurado: {}".format(elemento))

resultado = busca_binaria(lista, elemento)

if resultado == False:
    print("O elemento nao foi encontrado")
elif resultado == -2:
    print("Lista nao ordenada")
