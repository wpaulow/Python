def multiplo(n1, n2):
    if n1 % n2 == 0:
        return "é multiplo"
    else:
        return "não é multiplo"


# Programa principal
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print("O primeiro número %s do segundo" % multiplo(num1, num2))
