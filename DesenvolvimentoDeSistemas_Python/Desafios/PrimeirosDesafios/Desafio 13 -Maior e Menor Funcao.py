#Retornar o maior número de dois

def maior_ou_menor(a,b):
    if a > b:
        return "é maior"
    else:
        return "não é maior"



#Programa Principal
num1 = int(input("Digite o primeiro número:")) # Entrada de dados
num2 = int(input("Digite o segundo número:")) # Entrada de dados

print("%d %s que %d." % (num1, maior_ou_menor(num1,num2), num2))
