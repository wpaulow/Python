class CalculadoraRetangulo:

    def __init__(self,ladoMaior, ladoMenor):
        self.ladoMaior = ladoMaior
        self.ladoMenor = ladoMenor
        self.resultado = 0


    def area(self):
        self.resultado = self.ladoMaior * self.ladoMenor
        return self.resultado


    def perimetro(self):
        self.resultado =  2 * self.ladoMaior + 2 * self.ladoMenor
        return self.resultado
