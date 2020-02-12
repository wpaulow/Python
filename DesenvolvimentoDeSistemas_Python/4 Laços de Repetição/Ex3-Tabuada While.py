# Exemplo 3 - Utilizando o While
x = 0  # Define x como 0
num1 = int(input("Digite o número da tabuada desejada:"))  # Recebe o numero
while x <= 10:  # Enquanto x for menor ou igual a 10
    result = num1 * x  # Resultado recebe o numero vezes o valor atual de x
    print("%d X %d = %d" % (num1, x, result))  # Exibe os valores na tela
    x += 1  # Acrescenta +1 ao valor de x
