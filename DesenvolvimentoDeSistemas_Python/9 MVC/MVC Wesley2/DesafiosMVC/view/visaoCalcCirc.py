class VisaoCalcCirculo:

    def start(self):
        print("Vamos calcular a área e o perímetro de círculos?!")

    def getRaio(self): #Método para obter o valor do número 1
        raio = float(input("Digite o raio:"))
        return raio

    def getOper(self):
        print("1-Área do Círculo\n2-Perímetro do Círculo")
        op = int(input("Digite a operação desejada:"))
        return op

    def exibirErroOp(self):
        print("Opção Inválida!")

    def exibirResultado(self,resultado):
        print("O resultado é %5.2f" % resultado)
