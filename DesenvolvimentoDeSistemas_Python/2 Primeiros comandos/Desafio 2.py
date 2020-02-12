# Desafio 2 - Aumento de Salário
salario = float(input("Digite um valor do salário:"))  # Recebe o valor e converte para float
percAumento = float(input("Digite a porcentagem de aumento(Somente numeros):"))  # Recebe o valor e converte para float
novoSalario = salario + salario*percAumento/100
print("O novo salario é R$ %5.2f!!! " % novoSalario)
