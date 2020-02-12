'''Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
que é a quantia de imposto sobre vendas expressa em porcentagem; e custo, que é o valor de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas. '''

def somaImposto(txImp, preco):
    return preco * (1 + txImp/100)

precoProd = float(input("informe o valor do produto:"))
txImp = float(input("Informe o percentual de taxa de imposto:"))
print("o valor com a taxa é de %5.2f" % (somaImposto(txImp,precoProd)))