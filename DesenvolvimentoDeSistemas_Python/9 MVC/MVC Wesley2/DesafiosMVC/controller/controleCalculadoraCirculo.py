from model.calculadoraCirculo import CalculadoraCirculo

from view.visaoCalcCirc import VisaoCalcCirculo


class ControleCalculadora:


    def __init__(self):
        self.raio = 0
        self.opcao = ""
        self.calc = 0
        self.telaCalc = VisaoCalcCirculo()


    def lerDados(self):
        self.raio = self.telaCalc.getRaio()
        self.opcao = self.telaCalc.getOper()
        self.calculos()


    def calculos(self):
        op = self.opcao
        self.calc = CalculadoraCirculo(self.raio)

        if op == 1:
            resposta = self.calc.area()
        elif op == 2:
            resposta = self.calc.perimetro()
        else:
            resposta = "erroOp"
        self.resultado(resposta)


    def resultado(self, resposta):
        if resposta == "erroOp":
            self.telaCalc.exibirErroOp()
        else:
            self.telaCalc.exibirResultado(resposta)
