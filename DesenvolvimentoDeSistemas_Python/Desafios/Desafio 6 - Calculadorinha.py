#Calculadorazinha. Solicitar dois números e a escolha da operação matemática que se quer realizar com eles.

print("Calculadorazinha")
num1 = float(input("Digite um número qualquer:"))
num2 = float(input("Digite mais um número a sua escolha:"))
verificacao = int(input("Digite 1 para somá-los, digite 2 para subtrair o segundo do primeiro, digite 3 para "
                     "multiplicá-los e digite 4 se quer dividir o primeiro pelo segundo valor:"))

if verificacao == 1:
    print("O resultado dessa soma é: " , num1 + num2 , ".")

elif verificacao == 2:
    print("O resultado da subtração do primeiro algarismo pelo segundo é: " , num1 - num2)

elif verificacao == 3:
    print("O resultado da multiplicação desses números é: " , num1 * num2)

elif verificacao == 4:
    print("O resultado da divisão do primeiro número pelo segundo é: " , num1 / num2)

else:
    print("Você digitou uma opção inválida.")

