lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0

for numero in lista:
    while x<=10:
        resultado = numero * x
        print("%d X %d = %d" % (numero, x, resultado))
        x += 1
    x=0
    print("="*100)
'''Perguntar por que deu errado = x=0!!'''
