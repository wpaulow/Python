from model.calculadora import Calculadora

from view.visaoCalculadora import VisaoCalculadora



class ControleCalculadora:

    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.opcao = ""
        self.calc = 0
        self.telaCalc = VisaoCalculadora()

    def lerDados(self):
        self.numero1 = self.telaCalc.getnum1()
        self.numero2 = self.telaCalc.getnum2()
        self.opcao = self.telaCalc.getoper()
        self.calculos()

    def calculos(self):
        op = self.opcao
        self.calc = Calculadora(self.numero1, self.numero2)

        if op == 1:
            resposta = self.calc.somar()
        elif op == 2:
            resposta = self.calc.subtrair()
        elif op == 3:
            resposta = self.calc.multiplicar()
        elif op == 4:
            resposta = self.calc.dividir()
        else:
            resposta = "erroOp"
        self.resultado(resposta)

    def resultado(self, resposta):
        if resposta == "erroOp":
            self.telaCalc.exibirerroOp()
        elif resposta == "erroDiv":
            self.telaCalc.exibirerroDiv()
        else:
            self.telaCalc.exiberesult(resposta)



