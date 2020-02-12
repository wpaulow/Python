class MinhaCalculadora:  # Define o nome da classe
    # __init__() é o método inicializador da classe recebendo
    # 2 parametros operando1 e operando2
    def __init__(self, num1, num2):  # self faz referencia ao proprio obj
        self.resultado = 0  # então estamos definindo os atributos
        self.operando1 = num1  # do proprio obj instanciado e os tornando
        self.operando2 = num2  # acessiveis pros outros metodos(def)

    def somar(self):  # Definição do método somar
        self.resultado = self.operando1 + self.operando2

    def subtrair(self):  # Definição do método subtrair
        self.resultado = self.operando1 - self.operando2

    def multiplicar(self):  # Definição do método multiplicar
        self.resultado = self.operando1 * self.operando2

    def dividir(self):  # Definição do método dividir
        self.resultado = self.operando1 / self.operando2
