'''Programa que pede para o usuário digitar um número e então retorna True para par e False para ímpar. Utilizando
funções.'''

def epar(x):
    return x % 2 == 0


#Programa Principal
num = int(input("Digite um número:"))
print("O número é par?", epar(num))

'''O condicional == retorna valores booleanos.'''
