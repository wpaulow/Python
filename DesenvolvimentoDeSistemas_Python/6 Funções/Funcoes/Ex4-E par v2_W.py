def epar(x): # Definição da função e seu parâmetro
    return x % 2 == 0 # Valor do retorno


def par_ou_impar(y): # Definição da função e seu parâmetro
    if epar(y): # Chamada da função passando parâmetro
        return "par." # Valor de retorno
    else:
        return "ímpar." # Valor de retorno


#Programa Principal
num = int(input("Digite um número:")) # Entrada de dados
print("%d é %s" % (num, par_ou_impar(num))) # Chamada da função
