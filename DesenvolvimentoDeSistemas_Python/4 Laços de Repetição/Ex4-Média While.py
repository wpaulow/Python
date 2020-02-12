# Exemplo 4 - Utilizando o While
nome = input("Digite o nome do aluno:")  # Recebe o Nome
n = 0  # Cria um contador e atribui 0 a ele
qtd = int(input("Digite quantas notas serão utilizadas para calcular a média:"))
# Recebe a quantidade de notas
total = 0  # Cria um acumulador que vai possuir o total
while qtd > n:
        dig = float(input("Digite a nota do aluno:"))  # Recebe a nota
        total = total + dig  # total recebe seu atual valor + a nota
        n += 1  # Acrescenta +1 ao valor de n
media = total / qtd  # Calcula a media e atribui à variavel
if media >= 7:  # Se a média for maior ou igual a 7
        status = "aprovado"  # Status recebe aprovado
else:  # Senão
        status = "reprovado"  # Status recebe reprovado
print("A média do %s foi %5.2f, portanto ele está %s!!!" % (nome, media, status))
# Escreve a média, e se está ou não aprovado
