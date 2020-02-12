# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma_tres(a,b,c):
    return a + b + c

a = int(input("Digite um número:"))
b = int(input("Digite um número:"))
c = int(input("Digite um número:"))
print(soma_tres(a,b,c))