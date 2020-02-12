# Exemplo 4 - Convertendo tipos
num1 = int(input("Digite um número:"))  # Recebe o valor e converte para inteiro
num2 = int(input("Digite um número:"))  # Recebe o valor e converte para inteiro
soma = num1 + num2
print("A soma dos dois números é ", soma)
print("%d + %d = %d" % (num1, num2, soma))
'''OBS: Podemos utilizar % para faciltar o nosso print, podendo marcar a posição
onde aparecerá a variavel, subistituindo isto:
print(num1,"+", num2, "=", soma)
Por isto:
print("%d + %d = %d" % (num1, num2, soma))
%d ou %i pra os inteiros, %f para o float, %s pra string e assim vai...
'''