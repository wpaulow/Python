from circulo import CalcularCirculo

nraio= float(input("Digite o raio: "))

calc = CalcularCirculo(nraio)

calc.area()

print("A área é: " , calc.resultado, "\n")

calc.perimetro()

print("O perímetro é: " , calc.resultado)
