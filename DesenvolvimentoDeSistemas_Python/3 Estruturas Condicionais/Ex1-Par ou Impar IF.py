# Exemplo 1 - Utilizando o IF
num = float(input("Digite um núero:"))  # Recebe um número
# Quando utilizamos o módulo(%) pegamos o resto da divisão inteira
resto = (num % 2)
if resto == 1:  # Se o resto é igual 1
    resultado = "impar"  # Resultado recebe impar
if resto == 0:  # Se o resto é igual 0
    resultado = "par"  # Resultado recebe par
print("O número digitado é %s!" % resultado)  # Exibe o resultado
