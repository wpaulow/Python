from model.calculadoraCirculo import CalculadoraCirculo
from model.calculadoraRetangulo import CalculadoraRetangulo
from view.visaoGeometria import VisaoGeometria


class ControleCalculadora:


    def __init__(self):
        self.raio = 0
        self.opcao = ""
        self.forma = ""
        self.calc = 0
        self.telaCalc = VisaoGeometria()


    def lerDados(self):
        self.forma = self.telaCalc.getForma()
        self.opcao = self.telaCalc.getOper()
        self.opcaoRet = self.telaCalc.getOperRet()
        self.raio = self.telaCalc.getRaio()
        self.ladoMaior = self.telaCalc.getLadoMaior()
        self.ladoMenor = self.telaCalc.getLadoMenor()
        self.calculos()


    def calculos(self):
        forma = self.forma
        if forma == 1:
            opRet = self.forma
            self.calc = CalculadoraRetangulo(self.ladoMenor, self.ladoMaior)

            if opRet == 1:
                resposta = self.calc.area()
            elif opRet == 2:
                resposta = self.calc.perimetro()
            else:
                resposta = "erroOp"
            self.resultado(resposta)


        elif forma == 2:
            op = self.opcao
            self.calc = CalculadoraCirculo(self.raio)

            if op == 1:
                resposta = self.calc.area()
            elif op == 2:
                resposta = self.calc.perimetro()
            else:
                resposta = "erroOp"
            self.resultado(resposta)

        else:
            print("Forma inexistente.")


    def resultado(self, resposta):
        if resposta == "erroOp":
            self.telaCalc.exibirErroOp()
        else:
            self.telaCalc.exibirResultado(resposta)
