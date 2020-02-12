def maior(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


# Programa principal
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print("O número maior é ", maior(num1, num2))
