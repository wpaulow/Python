import sys

print("Bem vindo a calculadora!\n")
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
print("Agora digite o número referente a sua opção:")
print("1 para Soma.\n2 para Subtração.\n3 para Multiplicação.\n4 para Divisão.")
op = int(input(":"))
if op == 1:
    result = num1 + num2
elif op == 2:
    result = num1 - num2
elif op == 3:
    result = num1 * num2
elif op == 4:
    result = num1 / num2
else:
    print("Por favor inicie novamente e escolha um aopção de 1 a 4!")
    sys.exit()
print("O resultado é %5.2f" % result)
