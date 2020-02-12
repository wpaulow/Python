# Arquivo principal do programa.
from circulo import Circulo
# Do arquivo circulo importe a classe Circulo

raio = float(input("Quantos centimetros tem o raio: "))  # Entrada de dados

meuCirculo = Circulo(raio)  # Na variavel meuCirculo cria um novo
# objeto do tipo Circulo, passando raio como parâmetro

meuCirculo.calc_area()  # Chama o método calc_area
print("A area do circulo é %5.2fcm²!" % meuCirculo.area)

meuCirculo.calc_perimetro()  # Chama o método calc_perimetro
print("O perímetro do circulo é %5.2fcm!" % meuCirculo.perimetro)
