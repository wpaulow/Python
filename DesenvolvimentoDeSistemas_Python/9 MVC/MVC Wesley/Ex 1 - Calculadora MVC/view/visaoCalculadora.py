class VisaoCalculadora: #Definição da classe

    def start(self): #Definição do método que inicia a interação com o usuário
        print("Bem vindo a minha calculadora MVC!!!")


    def getnum1(self): #Método para obter o valor do número 1
        numero1 = float(input("Digite o primeiro número:"))
        return numero1

    def getnum2(self):
        numero2 = float(input("Digite o segundo número:"))
        return numero2

    def getoper(self):
        print("1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n")
        op = int(input("Digite a operação desejada:"))
        return op

    def exibirerroOp(self):
        print("Opção Inválida!")

    def exibirerroDiv(self):
        print("Não existe divisão por 0 (zero)")

    def exiberesult(self,resultado):
        print("O resultado é %5.2f" % resultado)

