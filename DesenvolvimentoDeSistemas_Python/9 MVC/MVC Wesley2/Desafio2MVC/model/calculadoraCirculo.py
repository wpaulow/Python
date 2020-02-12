class CalculadoraCirculo:

    def __init__(self,raio):
        self.raio = raio
        self.resultado = 0


    def area(self):
        self.resultado = 3.1416 * (self.raio ** 2)
        return self.resultado


    def perimetro(self):
        self.resultado =  2 * 3.1416 * self.raio
        return self.resultado