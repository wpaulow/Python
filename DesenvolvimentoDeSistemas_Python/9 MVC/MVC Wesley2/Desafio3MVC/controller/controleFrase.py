from model.frase import ConverteCase
from view.visaoFrase import VisaoFrase

class ControleFrase:

    def __init__(self):
        self.telaFrase = VisaoFrase()
        self.frase = ""
        self.forma = ""

    def lerDados(self):
        self.frase = self.telaFrase.getFrase()
        self.forma = self.telaFrase.getForma()
        self.converteFrase()


    def converteFrase(self):
        forma = self.forma
        self.convertCase = ConverteCase(self.frase)

        if forma == 1:
            resposta = self.convertCase.maiuscula()
        elif forma == 2:
            resposta = self.convertCase.minuscula()
        elif forma == 3:
            resposta = self.convertCase.primeiraMaiuscula()
        elif forma == 4:
            resposta = self.convertCase.todasMaiusculas()
        else:
            resposta = "erroOp"
        self.resultado(resposta)


    def resultado(self, resposta):
        if resposta == "erroOp":
            self.telaCalc.exibirErroOp()
        else:
            self.telaFrase.exibirResultado(resposta)

