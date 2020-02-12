class Triangulo:


    def __init__(self, lado1, lado2, base, altura):
        self.perimetro = 0
        self.area = 0
        self.lado1 = lado1
        self.lado2 = lado2
        self.base = base
        self.altura = altura


    def calc_perimetro(self):
        self.perimetro = self.lado1 + self.lado2 + self.base


    def calc_area(self):
        self.area = self.base * self.altura



