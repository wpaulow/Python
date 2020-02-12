lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num1 = int(input("Digite o número da tabuada desejada:"))  # Recebe o numero

for posicao in lista:
    result = num1 * posicao  # Resultado recebe o numero vezes o valor atual de x
    print("%d X %d = %d" % (num1, posicao, result))  # Exibe os valores na tela