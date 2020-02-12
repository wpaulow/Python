def media(*valores):  # Definição da função e seu parâmetro
    soma = 0
    qtd = 0
    for num in valores:
        soma += num
        qtd += 1
    return soma / qtd  # Valor de retorno


# programa principal
print("Média: %5.2f" % media(10))  # Chamada da função
print("Média: %5.2f" % media(10, 9))
print("Média: %5.2f" % media(10, 8, 9, 10))
print("Média: %5.2f" % media(6, 7, 9, 8, 8, 9))
