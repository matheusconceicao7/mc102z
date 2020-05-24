def tupla_float_int(x):
    x = x[1:-1]       # remove parenteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])   # converte primeiro elemento para float
    i = int(x[1])     # converte segundo elemento para int
    return (f, i)     # retorna tupla


notas_lab = [tupla_float_int(x) for x in input().split()]

prova1, prova2 = [float(x) for x in input().split()]

soma_notas_lab = 0
soma_pesos_lab = 0
for nota_lab in notas_lab:
    soma_notas_lab += nota_lab[0]*nota_lab[1]
    soma_pesos_lab += nota_lab[1]

media_lab = soma_notas_lab / soma_pesos_lab
media_provas = (prova1*3 + prova2*4) / 7

print("Media das tarefas de laboratorio: {:.1f}".format(media_lab))
print("Media das provas: {:.1f}".format(media_provas))

if (media_lab >= 5 and media_provas >= 5):
    media_final = round(0.3 * media_lab + 0.7 * media_provas, 1)
elif (media_lab >= 2.5 and media_provas >= 2.5):
    exame = float(input())
    media_preliminar = round(min(4.9, 0.3 * media_lab + 0.7 * media_provas), 1)
    media_final = round((media_preliminar + exame) / 2, 1)
    print("Media preliminar: {:.1f}".format(media_preliminar))
    print("Nota no exame: {:.1f}".format(exame))
else:
    media_final = round(min(media_lab, media_provas), 1)

if (media_final >= 5):
    print("Aprovado(a) por nota e frequencia")
else:
    print("Reprovado(a) por nota")
print("Media final: {:.1f}".format(media_final))
