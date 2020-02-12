# Responder se o primeiro número é múltiplo do segundo ou não

def multiplo_se(a,b):
    if a % b == 0:
        return "é múltiplo"
    else:
        return "não é múltiplo"


numA = int(input("Digite um número:"))
numB = int(input("Digite mais um número:"))
print("%d %s de %d." % (numA, multiplo_se(numA,numB), numB))
