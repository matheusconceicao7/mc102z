# A entrada do seu programa será composta por duas linhas, a primeira contendo
# um float representando o valor da fatura e a segunda um int representando o
# número de dias em atraso.
#
# 99.99
# 3
#
# A saída deverá ser apresentada como descrito a seguir, com strings sem acento
#
# Valor: o valor lido da entrada;
# Multa: 2% do valor da fatura.
# Juros: 0.033% do valor da fatura multiplicado pelo número de dias em atraso.
# Valor total: soma do valor inicial com valor da multa e dos juros.
# Pagamento minimo para renegociacao: 10% do valor total.
# Para a entrada da seção anterior, a saída será:
#
# Valor: R$ 99.99
# Multa: R$ 2.00
# Juros: R$ 0.10
# Valor total: R$ 102.09
# Valor minimo para renegociacao: R$ 10.20


valor = float(input())
dias_atraso = int(input())

multa = 0.02 * valor
juros = 0.00033 * valor * dias_atraso
valor_total = valor + multa + juros
pagamento_minimo = 0.1 * valor_total

print("Valor: R$", format(valor, ".2f"))
print("Multa: R$", format(multa, ".2f"))
print("Juros: R$", format(juros, ".2f"))
print("Valor total: R$", format(valor_total, ".2f"))
print("Valor minimo para renegociacao: R$", format(pagamento_minimo, ".2f"))
