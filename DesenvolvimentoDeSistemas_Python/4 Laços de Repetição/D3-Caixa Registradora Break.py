print("Bem vindo ao mercadinho!!!")
print("1-Trakinas R$ 2.00")
print("2-Doritos R$ 3.50")
print("3-Coca-Cola 3 L R$ 8.50")
print("4-Toddynho R$ 3.00")
total = 0.0
while True:
    cod = int(input("Digite o código do produto ou 0 (zero) para sair:"))
    if cod == 0:
        break
    if cod > 4 or cod < 0:
        print("Eesse código é inválido, tente novamente com um código de 1 a 4\n")
    else:
        qtd = int(input("Digite a quantidade desse produto:"))
        if cod == 1:
            preco = qtd * 2.00
            print("O valor deste produto foi %5.2f!" % preco)
        elif cod == 2:
            preco = qtd * 3.50
            print("O valor deste produto foi %5.2f!" % preco)
        elif cod == 3:
            preco = qtd * 8.50
            print("O valor deste produto foi %5.2f!" % preco)
        elif cod == 4:
            preco = qtd * 3.00
            print("O valor deste produto foi %5.2f!" % preco)
        total = total + preco

print("O total da sua compra foi %5.2f!" % total)
