# Exemplo 4 - IMC utilizando o IF, ELSE e ELIF
altura = float(input("Digite sua altura:"))  # Recebe a altura
peso = float(input("Digite o seu peso:"))  # Recebe o peso
imc = peso / (altura * altura)  # Calcula o IMC
print("Seu IMC é %5.2f" % imc)  # Exibe o IMC
if imc <= 17.00:  # Se o IMC for menor ou igual 17
    print("Muito abaixo do peso!")  # Escreve a categoria do IMC
elif imc <= 18.49:  # SenãoSe o IMC for menor ou igual 18.49
    print("Abaixo do peso!")
elif imc <= 24.99:  # SenãoSe o IMC for menor ou igual 24.99
    print("Peso normal!")
elif imc <= 29.00:  # SenãoSe o IMC for menor ou igual 29.00
    print("Acima do peso!")
elif imc <= 34.99:  # SenãoSE o IMC for menor ou igual 34.99
    print("Obesidade I!")
elif imc <= 39.99:  # SenãoSe o IMC for menor ou igual 39.99
    print("Obesidade II (severa)!")
else:  # Senão
    print("Obesidade III (mórbida)!")
