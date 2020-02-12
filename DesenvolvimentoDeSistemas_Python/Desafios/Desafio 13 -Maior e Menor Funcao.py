#Retornar o maior número de dois

def maiormenor(a, b):
    return a > b


def maior_ou_menor(x,y):
    if maiormenor(x,y):
        return "é maior"
    else:
        return "não é maior"



#Programa Principal
num1 = int(input("Digite o primeiro número:")) # Entrada de dados
num2 = int(input("Digite o segundo número:")) # Entrada de dados

print("%d %s que %d." % (num1, maior_ou_menor(num1,num2), num2))
