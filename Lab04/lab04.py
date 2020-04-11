# Considere que A é a medida do maior lado do triângulo e B e C são as outras
# medidas. Um teste simples para classificar o triângulo de acordo com as
# medidas do ângulos internos é a seguinte:
#
# Triângulo acutângulo: A² < B² + C²
# Triângulo retângulo: A² = B² + C²
# Triângulo obtusângulo: A² > B² + C²

x = float(input())
y = float(input())
z = float(input())

# Verifica maior lado e atribui a 'a'
if(x >= y and x >= z):
    a = x
    b = y
    c = z
elif(y >= x and y >= z):
    a = y
    b = x
    c = z
else:
    a = z
    b = x
    c = y
# Verifica se triangulo eh valido
if((a >= b + c) or a <= 0.0 or b <= 0.0 or c <= 0.0):
    print("Valores invalidos na entrada")
else:
    # Classifica de acordo com angulo interno
    if(pow(a, 2) < pow(b, 2) + pow(c, 2)):
        classif_angulo = "Triangulo acutangulo"
    elif(pow(a, 2) == pow(b, 2) + pow(c, 2)):
        classif_angulo = "Triangulo retangulo"
    else:
        classif_angulo = "Triangulo obtusangulo"

    # Classifica de acordo com medida dos lados
    if(a != b and b != c and c != a):
        classif_lados = "Triangulo escaleno"
    elif(a == b and b == c and c == a):
        classif_lados = "Triangulo equilatero"
    else:
        classif_lados = "Triangulo isosceles"

    print(classif_lados)
    print(classif_angulo)
