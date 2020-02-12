'''Programa que solicita o código do produto e a quantidade, calcule e exiba o total do item e então solicite
novamente código e quantidade do produto até que o usuário digite 0 (zero). Por fim exiba o total da compra.'''
total = 0
while True:
    codigo = int(input("Digite 1 para Trakinas, digite 2 para Doritos, digite 3 para Coca-Cola e digite 4 para"
                       "Toddynho e digite 0 para finalizar suas compras:"))
    if codigo == 0:
        break

    if codigo == 1:
        qntdTrak = int(input("Digite a quantidade de Trakinas:"))
        print("A quantidade de " , qntdTrak , " Trakinas totalizou R$" , qntdTrak * 2)
        total = total + qntdTrak * 2

    if codigo == 2:
        qntdDori = int(input("Digite a quantidade de Doritos:"))
        print("A quantidade de ", qntdDori, " Doritos totalizou R$", qntdDori * 3.5)
        total = total + qntdDori * 3.5

    if codigo == 3:
        qntdCoca = int(input("Digite a quantidade de Cocas:"))
        print("A quantidade de ", qntdCoca, " Cocas totalizou R$", qntdCoca * 8.5)
        total = total + qntdCoca * 8.5

    if codigo == 4:
        qntdTod = int(input("Digite a quantidade de Toddynhos:"))
        print("A quantidade de ", qntdTod, " Toddynhos totalizou R$", qntdTod * 3)
        total = total + qntdTod * 3

print("O total da compra é de R$" , total)