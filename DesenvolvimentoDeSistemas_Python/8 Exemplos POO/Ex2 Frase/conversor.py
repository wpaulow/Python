class Conversor:
    def __init__(self, frase):
        self.resultado = 0
        self.frase = frase

    def maiuscula(self):
        self.resultado = self.frase.upper()
