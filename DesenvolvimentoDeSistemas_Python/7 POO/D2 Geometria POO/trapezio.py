class Trapezio:


    def __init__(self, baseMaior, baseMenor, lado1, lado2, altura):
        self.perimetro = 0
        self.area = 0
        self.baseMaior = baseMaior
        self.baseMenor = baseMenor
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura


    def calc_area_trapezio(self):
        self.area = self.baseMaior + self.baseMenor * self.altura / 2


    def calc_perimetro_trapezio(self):
        self.perimetro = self.baseMenor + self.baseMaior + self.lado1 + self.lado2


