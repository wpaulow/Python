# Arquivo principal do programa.
from circulo import Circulo  # Do arquivo circulo importe a classe Circulo
from retangulo import Retangulo  # Do arq retangulo importa a classe Retangulo
from triangulo import Triangulo
from trapezio import Trapezio


print("Escolha qual forma deseja utilizar nos calculos!")
forma = int(input("1-Circulo\n2-Retangulo\n3-Triangulo\n4-Trapézio\n->"))
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
elif forma == 3:
    ladoA = int(input("Digite um lado do triângulo: "))
    ladoB = int(input("Digite outro lado do triângulo: "))
    baseTri = int(input("Digite a base do triângulo:"))
    altTri = int(input("Digite a altura do triângulo: "))
    meuTriangulo = Triangulo(ladoA, ladoB, baseTri, altTri)
    meuTriangulo.calc_perimetro()
    print("O perímetro do triângulo é %5.2f cm." % meuTriangulo.perimetro)
    meuTriangulo.calc_area()
    print("A área do triângulo é %5.2f cm²." % meuTriangulo.area)
elif forma == 4:
    baseMaior = int(input("Digite a base maior do trapézio: "))
    baseMenor = int(input("Digite a base menor do trapézio: "))
    lado1 = int(input("Digite um dos lados do trapézio: "))
    lado2 = int(input("Digite o outro lado do trapézio: "))
    altura = int(input("Digite a altura do trapézio: "))
    meuTrapezio = Trapezio(baseMaior, baseMenor, lado1, lado2, altura)
    meuTrapezio.calc_area_trapezio()
    print("A área do trapézio é de %5.2fcm² " % meuTrapezio.area)
    meuTrapezio.calc_perimetro_trapezio()
    print("O perímetro do trapézio é de %5.2fcm " % meuTrapezio.perimetro)

else:
    print("Opição inválida...")
