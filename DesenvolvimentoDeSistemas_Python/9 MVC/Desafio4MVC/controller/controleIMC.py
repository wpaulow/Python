from model.imc import IMC
from view.visaoIMC import VisaoIMC

class ControleIMC:

    def __init__(self):
        self.telaIMC = VisaoIMC()
        self.peso = 0
        self.altura = 0


    def lerDados(self):
        self.peso = self.telaIMC.getPeso()
        self.altura = self.telaIMC.getAltura()
        self.calculoIMC()


    def calculoIMC(self):
        self.calcIMC = IMC(self.peso, self.altura)
        valor = self.calcIMC.calcularIMC()
        self.resultado(valor)


    def resultado(self, valor):
        self.telaIMC.exibirResultado(valor)
        self.categoria(valor)


    def categoria(self, valor):
        if valor < 18.5:
            self.telaIMC.exibirCategoriaAbaixoDoPeso()
        elif valor < 25:
            self.telaIMC.exibirCategoriaPesoNormal()
        elif valor < 30:
            self.telaIMC.exibirCategoriaSobrepeso()
        elif valor < 35:
            self.telaIMC.exibirCategoriaObesoI()
        elif valor < 40:
            self.telaIMC.exibirCategoriaObesoII()
        else:
            self.telaIMC.exibirCategoriaObesoIII()


