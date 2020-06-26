def interseccao(lista_a, lista_b):
    interseccao = [it for it in lista_a if it in lista_b]
    return sorted(interseccao)


def encontra_amizade_individualizada(nome, lista):
    for i in lista:
        if(nome in i):
            return i


nome = input()
nomes = []

while nome != '--':
    nomes.append(nome)
    nome = input()

nomes.sort()

par_amizade = input()
pares_amizade = []

while par_amizade != '--':
    pares_amizade.append(tuple(par_amizade.split()))
    par_amizade = input()


amizades_individualizadas = []
for index, nome in enumerate(nomes):
    amizades_individualizadas.append((nome, []))
    for par_amizade in pares_amizade:
        if nome in par_amizade:
            amigo = par_amizade[par_amizade.index(nome) - 1]
            amizades_individualizadas[index][1].append(amigo)

amigos_em_comum = []
for index, nome in enumerate(nomes):
    sublist = nomes[index+1:]
    for it in sublist:
        lista_a = encontra_amizade_individualizada(
            nome, amizades_individualizadas)[1]
        lista_b = encontra_amizade_individualizada(
            it, amizades_individualizadas)[1]
        amigos_em_comum.append(('{} {}'.format(nome, it), interseccao(
            lista_a, lista_b)))

for i in amigos_em_comum:
    print('{} : {}'.format(i[0], ', '.join(i[1])).rstrip())
