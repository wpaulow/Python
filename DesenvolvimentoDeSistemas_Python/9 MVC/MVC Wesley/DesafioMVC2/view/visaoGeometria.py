class VisaoGeometria:

    def start(self):
        print("Vamos calcular áreas e perímetros?!")

    def getForma(self):
        print("1-Retângulo\n 2-Círculo")
        forma = int(input("Digite a forma geométrica desejada:"))
        return forma

    def getOperRet(self):
        print("1-Área do Retângulo\n2-Perímetro do Retângulo")
        opRet = int(input("Digite a operação desejada:"))
        return opRet

    def getLadoMenor(self):
        ladoMenor = print("Digite o lado menor:")
        return ladoMenor

    def getLadoMaior(self):
        ladoMaior = print("Digite o lado maior:")
        return ladoMaior

    def exibirResultadoRet(self,resultado):
        print("O resultado é %5.2f" % resultado)

    def getOper(self):
        print("1-Área do Círculo\n2-Perímetro do Círculo")
        op = int(input("Digite a operação desejada:"))
        return op

    def getRaio(self): #Método para obter o valor do número 1
        raio = float(input("Digite o raio:"))
        return raio

    def exibirErroOp(self):
        print("Opção Inválida!")

    def exibirResultado(self,resultado):
        print("O resultado é %5.2f" % resultado)
