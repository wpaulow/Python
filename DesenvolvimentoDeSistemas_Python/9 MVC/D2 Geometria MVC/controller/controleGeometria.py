from model.circulo import Circulo
# Da pasta model do arquivo circulo importe a classe Circulo
from model.retangulo import Retangulo
# Da pasta model do arq retangulo importa a classe Retangulo
from view.visaoGemetria import VisaoGeometria
# Da pasta view do arqu visaoGeometria importa a classe VisaoGeometria


class ControleGeometria:

    def __init__(self):
        self.telaGeometria = VisaoGeometria()
        self.meucirculo = 0
        self.meuretangulo = 0

    def decicdeforma(self):
        forma = self.telaGeometria.getforma()
        if forma == 1:  # Se foi escolhido a forma 1 (Circulo)
            self.calccirculo()
        elif forma == 2:  # Se foi escolhido a forma 2 (Retangulo)
            self.calcretangulo()
        else:
            self.telaGeometria.msgerro()

    def calccirculo(self):
        raio = self.telaGeometria.getraio()
        meucirculo = Circulo(raio)  # Na variavel meuCirculo cria um novo
        # objeto do tipo Circulo, passando raio como parâmetro
        area = meucirculo.calc_area()  # Chama o método calc_area
        perimetro = meucirculo.calc_perimetro()  # Chama o método calc_perimetro
        self.telaGeometria.exiberesultcirculo(area, perimetro)

    def calcretangulo(self):
        altura = self.telaGeometria.getaltuta()
        largura = self.telaGeometria.getlargura()
        meuretangulo = Retangulo(altura, largura)  # Na variavel meuretangulo cria um novo
        # objeto do tipo Retangulo, passando ladoMaior e ladoMenor como parâmetros
        area = meuretangulo.calc_area()  # Chama o método calc_area
        perimetro = meuretangulo.calc_perimetro()  # Chama o método calc_perimetro
        self.telaGeometria.exiberesultretangulo(area, perimetro)
