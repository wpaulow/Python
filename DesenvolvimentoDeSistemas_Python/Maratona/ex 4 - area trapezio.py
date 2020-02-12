def area_trapezio(a ,b, c):
    return (a+b)*c/2


print("Vamos calcular a área de um trapézio?")
baseMaior = int(input("Informe a base maior:"))
baseMenor = int(input("Informe a base menor:"))
altura = int(input("Informe a altura:"))

print(area_trapezio(baseMaior,baseMenor,altura))
