impedimento = False
documento_autorizacao = False
doacoes_12_meses = False
meses_desde_ultima_doacao = False
gravida = False
massa = float(input())
idade = int(input())
if(idade >= 16 and idade < 18):
    documento_autorizacao = input()
febre = input()
viagem_ext = input()
contato_covid = input()
primeira_doacao = input()
if(primeira_doacao == "N"):
    doacoes_12_meses = int(input())
if(primeira_doacao == "N" and doacoes_12_meses > 0):
    meses_desde_ultima_doacao = int(input())
sexo = input()
if(sexo == "F"):
    gravida = input()

print("Massa corporal:", massa)
print("Idade:", idade)
if(documento_autorizacao):
    print("Documento de autorizacao:", documento_autorizacao)
print("Febre ou sintomas gripais:", febre)
print("Viagem recente ao exterior:", viagem_ext)
print("Contato com caso de COVID-19:", contato_covid)
print("Primeira doacao:", primeira_doacao)
if(doacoes_12_meses is not False):
    print("Doacoes nos ultimos 12 meses:", doacoes_12_meses)
if(meses_desde_ultima_doacao):
    print("Meses desde ultima doacao:", meses_desde_ultima_doacao)
print("Sexo biologico:", sexo)
if(gravida):
    print("Gravida ou amamentando:", gravida)
if(massa < 50):
    print("Impedimento: abaixo da massa corporal minima")
    impedimento = True
if(idade < 16):
    print("Impedimento: menor de 16 anos")
    impedimento = True
if(idade < 18 and documento_autorizacao == "N"):
    print("Impedimento: menor de 18 anos sem consentimento dos responsaveis")
    impedimento = True
if(idade > 60 and primeira_doacao == "S"):
    print("Impedimento: maior de 60 anos e primeira doacao")
    impedimento = True
if(idade > 69):
    print("Impedimento: maior de 69 anos")
    impedimento = True
if(febre == "S"):
    print("Impedimento: febre ou sintomas gripais")
    impedimento = True
if(viagem_ext == "S"):
    print("Impedimento: viagem recente ao exterior")
    impedimento = True
if(contato_covid == "S"):
    print("Impedimento: contato com caso de COVID-19")
    impedimento = True
if((sexo == "M" and primeira_doacao == "N" and doacoes_12_meses >= 4) or (sexo == "F" and primeira_doacao == "N" and doacoes_12_meses > 3)):
    print("Impedimento: numero maximo de doacoes anuais foi atingido")
    impedimento = True
if((sexo == "M" and primeira_doacao == "N" and doacoes_12_meses > 0 and meses_desde_ultima_doacao < 2) or (sexo == "F" and doacoes_12_meses > 0 and primeira_doacao == "N" and meses_desde_ultima_doacao < 3)):
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado")
    impedimento = True
if(gravida == "S"):
    print("Impedimento: gravida ou amamentando")
    impedimento = True
if(not impedimento):
    print("Agende um horario para triagem completa")
