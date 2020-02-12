#Classe principal do programa
from calculadoras import MinhaCalculadora
# Do arquivo calculadora importe a classe MinhaCalculadora

numero1 = float(input("Digite o primeiro número: ")) #Entrada de dados
numero2 = float(input("Digite o segundo número: "))
calc = MinhaCalculadora(numero1,numero2)
'''Na variável calc cria um novo objeto do tipo MinhaCalculadora, passando numero1 e numero2
como parâmetros'''
op = input("Digite o sinal da operação matemática desejada (+ - * /): ")
if op == "+":
    calc.somar()
elif op == "-":
    calc.subtrair()
elif op == "*":
    calc.multiplicar()
elif op == "/":
    calc.dividir()
else:
    print("0pção inválida.")
if op ==  "+" or op ==  "-" or op ==  "*" or op ==  "/" :
    print("O Resultado é ", calc.resultado)
