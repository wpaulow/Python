# Arquivo principal do programa.
from circulo import Circulo  # Do arquivo circulo importe a classe Circulo
from retangulo import Retangulo  # Do arq retangulo importa a classe Retangulo
print("Escolha qual forma deseja utilizar nos calculos!")
forma = int(input("1-Circulo\n2-Retangulo\n->"))
if forma == 1:  # Se foi escolhido a forma 1 (Circulo)
    raio = float(input("Quantos centimetros tem o raio: "))  # Entrada de dados
    meuCirculo = Circulo(raio)  # Na variavel meuCirculo cria um novo
    # objeto do tipo Circulo, passando raio como parâmetro
    meuCirculo.calc_area()  # Chama o método calc_area
    print("A área do circulo é %5.2fcm²!" % meuCirculo.area)
    meuCirculo.calc_perimetro()  # Chama o método calc_perimetro
    print("O perímetro do circulo é %5.2fcm!" % meuCirculo.perimetro)
elif forma == 2:
    altura = int(input("Digite a medida da altura do retangulo: "))  # Entrada de dados
    largura = int(input("Digite a medida da largura do retangulo: "))
    meuRetangulo = Retangulo(altura, largura)  # Na variavel meuretangulo cria um novo
    # objeto do tipo Retangulo, passando ladoMaior e ladoMenor como parâmetros
    meuRetangulo.calc_area()  # Chama o método calc_area
    print("A área do retangulo é %5.2fcm²!" % meuRetangulo.area)
    meuRetangulo.calc_perimetro()  # Chama o método calc_perimetro
    print("O perímetro do retangulo é %5.2fcm!" % meuRetangulo.perimetro)
else:
    print("Opição inválida...")
