class MinhaCalculadora: #Define o nome da classe
    #__init__() é o método inicializador da classe recebendo
    # 2 parâmetros operando1 e operando2
    def __init__(self, operando1, operando2):
        self.resultado = 0 # self faz referência ao próprio objeto
        self.operando1 = operando1 # então estamos definindo os atributos
        self.operando2 = operando2 # do próprio objeto instanciado

    def somar(self): # Definição do método somar
        self.resultado = self.operando1 + self.operando2

    def subtrair(self): # Definição do método subtrair
        self.resultado = self.operando1 - self.operando2

    def multiplicar(self): # Definição do método multiplicar
        self.resultado = self.operando1 * self.operando2

    def dividir(self): # Definição do método dividir
        self.resultado = self.operando1 / self.operando2