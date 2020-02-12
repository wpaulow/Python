class Calculadora:  # Define o nome da classe
    # __init__() é o método inicializador da classe recebendo
    # 2 parametros operando1 e operando2
    def __init__(self, num1, num2):  # self faz referencia ao proprio obj
        self.operando1 = num1  # então estamos definindo os atributos
        self.operando2 = num2  # do proprio obj instanciado e os tornando
        # acessiveis pros outros metodos(def)

    def somar(self):  # Definição do método somar
        resultado = self.operando1 + self.operando2
        return resultado

    def subtrair(self):  # Definição do método subtrair
        resultado = self.operando1 - self.operando2
        return resultado

    def multiplicar(self):  # Definição do método multiplicar
        resultado = self.operando1 * self.operando2
        return resultado

    def dividir(self):  # Definição do método dividir
        if self.operando2 == 0:
            return "erroDiv"
        else:
            resultado = self.operando1 / self.operando2
            return resultado
