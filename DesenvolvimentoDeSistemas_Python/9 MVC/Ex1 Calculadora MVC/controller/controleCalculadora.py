from model.calculadora import Calculadora
# Da pasta model do arquivo calculadora importe a classe Calculadora
from view.visaoCalculadora import VisaoCalculadora
# Da pasta view do arquivo visaoCalculadora importe a classe VisaoCalculadora


class ControleCalculadora:  # Definição da classe

    def __init__(self):  # Metodo inicializador
        self.numero1 = 0  # Inicia todas as variaveis vazias
        self.numero2 = 0  # Usando o self essas variaveis estarão
        self.opcao = ""  # acessiveis em todos os metodos(def), sem o self
        self.calc = 0  # só poderiam ser usadas no def onde foram criadas
        self.telaCalc = VisaoCalculadora()  # Instancia um objeto view

    def lerdados(self):  # Metodo para obter os dados da VisaoCalculadora
        self.numero1 = self.telaCalc.getnum1()  # Obtém o num1 através view
        self.numero2 = self.telaCalc.getnum2()  # Obtém o num2 através view
        self.opcao = self.telaCalc.getoper()  # Obtém o oper através view
        self.calculos()  # Chama o metodo calculos

    def calculos(self):  # Método que realiza os calculos
        op = self.opcao  # Inicia a variavel op com a opção ecolhida
        self.calc = Calculadora(self.numero1, self.numero2)  # Na variavel clac cria
        # um novo objeto do tipo Cauculadora, passando num1 e num2 como parâmetros
        if op == "1":  # Se a opção for 1
            resposta = self.calc.somar()  # Executa o método somar do obj calc
        elif op == "2":  # Se a opção for 2
            resposta = self.calc.subtrair()  # Executa o método subtrair do obj calc
        elif op == "3":  # Se a opção for 3
            resposta = self.calc.multiplicar()  # Executa o método multiplicar do obj calc
        elif op == "4":  # Se a opção for 4
            resposta = self.calc.dividir()  # Executa o método dividir do obj calc
        else:  # Se não for nenhuma das opções acima
            resposta = "erroOp"  # Resposta recebe erro de opção
        self.resultado(resposta)  # Chama o método resultado passando erro como parâmetro

    def resultado(self, resposta):  # Método que exibe o feedback ao usuário
        if resposta == "erroOp":  # Se resposta for erro de opção
            self.telaCalc.exibeerroOp()  # Chama o método do view que exibe a msg de erro
        elif resposta == "erroDiv":  # Se resposta for erro de divisão por zero
            self.telaCalc.exibeerroDiv()  # Chama o método do view que exibe a msg de erro
        else:  # Senão
            self.telaCalc.exiberesult(resposta)  # Chama o método do view
            # que exibe o resultado para o usuário
