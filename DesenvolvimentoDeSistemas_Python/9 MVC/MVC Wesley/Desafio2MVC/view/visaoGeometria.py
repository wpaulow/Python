class VisaoGeometria:

    def start(self):
        print("Vamos calcular áreas e perímetros?!")


    def getForma(self):
        forma = int(input("Digite a forma geométrica desejada:\n1-Retângulo\n2-Círculo"))
        return forma


    def getOperRetangulo(self):
        operacaoRetangulo = int(input("Digite a operação desejada:\n1-Área do Retângulo\n2-Perímetro do Retângulo"))
        return operacaoRetangulo


    def getLadoMenor(self):
        ladoMenor = int(input("Digite o lado menor:"))
        return ladoMenor


    def getLadoMaior(self):
        ladoMaior = int(input("Digite o lado maior:"))
        return ladoMaior


    def getOperCirculo(self):
        operacaoCirculo = int(input("Digite a operação desejada:\n1-Área do Círculo\n2-Perímetro do Círculo"))
        return operacaoCirculo


    def getRaio(self): #Método para obter o valor do número 1
        raio = float(input("Digite o raio:"))
        return raio


    def exibirErroOp(self):
        print("Opção Inválida!")


    def exibirResultadoPerimetro(self,resultado):
        print("O resultado é %5.2f" % resultado)


    def exibirResultadoArea(self,resultado):
        print("O resultado é %5.2f" % resultado)