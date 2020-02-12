# Desafio 3 - Desconto do produto
preco = float(input("Digite um valor do produto:"))  # Recebe o valor e converte para float
percDesc = float(input("Digite a porcentagem de desconto(Apenas números):"))  # Recebe o valor e converte para float
novoPreco = preco - preco*percDesc/100
print("O preço com desconto é R$ %5.2f!!! " % novoPreco)
