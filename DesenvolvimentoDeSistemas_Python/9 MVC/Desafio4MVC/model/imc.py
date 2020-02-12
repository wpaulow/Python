class IMC:

    def __init__(self, peso, alt):
        self.peso = peso
        self.alt = alt
        self.resultadoIMC = 0


    def calcularIMC(self):
        self.resultadoIMC = self.peso / (self.alt ** 2)
        return self.resultadoIMC


