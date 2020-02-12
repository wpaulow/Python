# Arquivo principal do programa.
from calculadora import MinhaCalculadora
# Do arquivo calculadora importe a classe MinhaCalculadora

numero1 = float(input("Digite o primeiro número: "))  # Entrada de dados
numero2 = float(input("Digite o segundo número: "))
calc = MinhaCalculadora(numero1, numero2)  # Na variavel clac cria um novo
# objeto do tipo MinhaCauculadora, passando numero1 e numero2 como parâmetros
op = input("Digite o sinal da operação matemática desejada( + - * / ): ")
if op == "+":
    calc.somar()  # Executa o método somar do obj calc
elif op == "-":
    calc.subtrair()  # Executa o método subtrair do obj calc
elif op == "*":
    calc.multiplicar()  # Executa o método multiplicar do obj calc
elif op == "/":
    calc.dividir()  # Executa o método dividir do obj calc
else:
    print("Opção inválida!!! ")
# Se foi utilizado um operador válido
if op == "+" or op == "-" or op == "*" or op == "/":
    print("O Resultado é ", calc.resultado)  # imprime a propriedade
    # resultado do objeto calc
