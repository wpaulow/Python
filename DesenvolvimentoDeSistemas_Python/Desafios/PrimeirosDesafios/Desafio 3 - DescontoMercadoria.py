'''Programa que solicita valor do produto e o desconto a ser calculado. Depois retorna o novo valor e
a quantia descontada'''

valorProd = float(input("Insira o valor da mercadoria:"))
desc = float(input("Informe o valor do desconto:"))
valorNovo = valorProd * (1 - desc/100)

print("O valor da mercadoria passa a ser R$%5.2f." % valorNovo)
print("E o valor correspondente ao desconto é de R$" , valorProd - valorNovo ,".")
sair = input("Digite X para fechar o programa: ")