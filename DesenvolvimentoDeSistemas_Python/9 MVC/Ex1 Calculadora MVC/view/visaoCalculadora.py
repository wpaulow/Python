class VisaoCalculadora:  # Definição da classe

    def start(self):  # Definição do método que inicia a interação com o usuario
        print("Bem vindo a minha calculadora MVC!!!")

    def getnum1(self):  # Método para obter a volar do numero 1
        numero1 = float(input("Digite o primeiro número: "))  # Entrada de dados
        return numero1  # Retorna o valor que o usuario digitou

    def getnum2(self): # Método para obter a volar do numero 2
        numero2 = float(input("Digite o segundo número: "))
        return numero2  # Retorna o valor que o usuario digitou

    def getoper(self): # Método para obter a volar do operador
        print("1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n ")
        op = input("Digite a opeção desejada: ")
        return op  # Retorna o valor que o ussuario digitou

    def exibeerroOp(self):  # Método que exibe a mensagem de erro
        print("Opção inválida!!! ")

    def exibeerroDiv(self):  # Método que exibe a mensagem de erro
        print("Não existe divisão por 0 (zero)!!! ")

    def exiberesult(self, resultado):  # Método que exibe o resultado
        print("O Resultado é %5.2f" % resultado)  # imprime a propriedade
