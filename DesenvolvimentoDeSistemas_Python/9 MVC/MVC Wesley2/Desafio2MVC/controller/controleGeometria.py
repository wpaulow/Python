from model.calculadoraCirculo import CalculadoraCirculo
from model.calculadoraRetangulo import CalculadoraRetangulo
from view.visaoGeometria import VisaoGeometria


class ControleCalculadora:


    def __init__(self):
        self.raio = 0
        self.opcao = ""
        self.forma = ""
        self.ladoMaior = 0
        self.ladoMenor = 0
        self.calcRetangulo = 0
        self.calcCirculo = 0
        self.telaCalc = VisaoGeometria()


    def lerDados(self):
        self.forma = self.telaCalc.getForma()
        if self.forma == 1:
            self.opcao = self.telaCalc.getOperRetangulo()
            self.ladoMaior = self.telaCalc.getLadoMaior()
            self.ladoMenor = self.telaCalc.getLadoMenor()
            self.calculosRetangulo()
        elif self.forma == 2:
            self.opcao = self.telaCalc.getOperCirculo()
            self.raio = self.telaCalc.getRaio()
            self.calculosCirculo()


    def calculosRetangulo(self):

            op = self.opcao
            self.calcRetangulo = CalculadoraRetangulo(self.ladoMenor, self.ladoMaior)

            if op == 1:
                resposta = self.calcRetangulo.area()
            elif op == 2:
                resposta = self.calcRetangulo.perimetro()
            else:
                resposta = "erroOp"
            self.resultado(resposta)


    def calculosCirculo(self):

            op = self.opcao
            self.calcCirculo = CalculadoraCirculo(self.raio)

            if op == 1:
                resposta = self.calcCirculo.area()
            elif op == 2:
                resposta = self.calcCirculo.perimetro()
            else:
                resposta = "erroOp"
            self.resultado(resposta)



    def resultado(self, resposta):
        if resposta == "erroOp":
            self.telaCalc.exibirErroOp()
        elif self.opcao == 1:
            self.telaCalc.exibirResultadoArea(resposta)
        else:
            self.telaCalc.exibirResultadoPerimetro(resposta)