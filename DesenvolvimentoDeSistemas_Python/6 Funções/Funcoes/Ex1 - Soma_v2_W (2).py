def soma(a,b): #Definição da função e de seus parâmetros
    return a + b # Valor do retorno


def multiplicacao(x,y):
    return x * y


#Programa Principal
num1 = int(input("Digite o primeiro número:")) # Entrada de dados
num2 = int(input("Digite o segundo número:")) # Entrada de dados

total = soma(num1,num2) # Chamada da função passando parâmetros
print("A soma dos dois números é ", total) # Saída de dados

total2 = multiplicacao(num1,num2)
print("A multiplicação dos dois números é", total2)
