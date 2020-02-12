class ConverteCase:

    def __init__(self, frase):
        self.frase = frase
        self.resultado = ""

    def minuscula(self):
        self.resultado = self.frase.lower()
        return self.resultado

    def maiuscula(self):
        self.resultado = self.frase.upper()
        return self.resultado

    def primeiraMaiuscula(self):
        self.resultado = self.frase.capitalize()
        return self.resultado

    def todasMaiusculas(self):
        self.resultado = self.frase.title()
        return self.resultado


