# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def qntd_digitos(x):
    return len(x)


num = input("Digite um número qualquer:")
print("O número possuí %d digitos." %qntd_digitos(num))