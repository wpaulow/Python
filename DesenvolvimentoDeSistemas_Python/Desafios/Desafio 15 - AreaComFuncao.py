# Receber o lado de um quadrado e retornar a sua área

def area (a):
    return a * a

numA = float(input("Informe o tamanho do lado do quadrado a ser calculada sua área:"))
print("A área do quadrado de lado %5.2f m é de %5.2f m²." % (numA, area(numA)))