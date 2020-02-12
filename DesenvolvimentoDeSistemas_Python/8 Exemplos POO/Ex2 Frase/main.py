from conversor import Conversor

frase = input("Digite uma frase")

convert = Conversor(frase)

convert.maiuscula()

print("A frase é" + convert.resultado)