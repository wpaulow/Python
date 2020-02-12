class CalcularCirculo:


    def __init__(self, raio):
        self.resultado = 0
        self.raio = raio


    def area(self):
        self.resultado = 3.1416 * (self.raio ** 2)

    def perimetro(self):
        self.resultado = 6.1832 * self.raio

