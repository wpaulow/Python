#Crie um programa que receba dois números e então exiba se o primeiro é maior, se o segundo é maior ou se são iguais.

print("Veja se o número é maior, menor ou se ambos são iguais logo abaixo:")
num1 = float(input("Digite um número qualquer:"))
num2 = float(input("Digite outro número:"))

if num1 > num2:
    print("O primeiro número é maior que o segundo inserido.")

elif num1 < num2:
    print("O segundo número que digitou é maior que o primeiro.")

else:
    print("Parece que você digitou o mesmo número.")