def triangulos (a,b,c):

    if a + b < c:
        return ("Não é triângulo")

    if a == b == c:
        return ("Equilátero")

    if a == b != c:
        return ("Isósceles")

    if a != b != c:
        return ("Escaleno")



ladoA = int(input("Digite o primeiro lado:"))

ladoB = int(input("Digite o segundo lado:"))

ladoC = int(input("Digite o terceiro lado:"))

print(triangulos(ladoA,ladoB,ladoC))
