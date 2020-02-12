def soma (a,b):
    return a+b


def subtracao (x,y):
    return x-y


def multiplicacao (i,j):
    return i*j


def divisao (n,m):
   if m>0:
       return n/m
   else:
       return ("Não existe divisão por zero. Tente outro valor!")



print("Calculadorazinha")
num1 = float(input("Digite um número qualquer:"))
num2 = float(input("Digite mais um número a sua escolha:"))

while True:

    verificacao = int(input("Digite 1 para somá-los, digite 2 para subtrair o segundo do primeiro, digite 3 para "
                         "multiplicá-los e digite 4 se quer dividir o primeiro pelo segundo valor:"))
    if verificacao == 5:
            break

    elif verificacao == 1:
        num1 = float(input("Digite um número qualquer:"))
        num2 = float(input("Digite mais um número a sua escolha:"))
        print("O resultado dessa soma é: " , soma(num1,num2), ".")

    elif verificacao == 2:
        num1 = float(input("Digite um número qualquer:"))
        num2 = float(input("Digite mais um número a sua escolha:"))
        print("O resultado da subtração do primeiro algarismo pelo segundo é: " , subtracao(num1,num2))

    elif verificacao == 3:
        num1 = float(input("Digite um número qualquer:"))
        num2 = float(input("Digite mais um número a sua escolha:"))
        print("O resultado da multiplicação desses números é: " , multiplicacao(num1,num2))

    elif verificacao == 4:
        num1 = float(input("Digite um número qualquer:"))
        num2 = float(input("Digite mais um número a sua escolha:"))
        print("O resultado da divisão do primeiro número pelo segundo é: " , divisao(num1,num2))

    else:
        print("Você digitou uma opção inválida.")
