class Calculadora: #faz todos os cálculos
    # __init__() é o método inicializador da classe recebendo
    # 2 parâmetros operando1 e operando2
    def __init__(self, num1, num2):
        self.operando1 = num1 # então estamos definindo os atributos
        self.operando2 = num2 # do próprio obj instanciado e os tornando


    def somar(self):
        resultado = self.operando1 + self.operando2
        return resultado

    def subtrair(self):
        resultado = self.operando1 - self.operando2
        return resultado

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        return resultado

    def dividir(self):
        if self.operando2 == 0:
            return "erroDiv"
        else:
            resultado = self.operando1 / self.operando2
            return resultado
