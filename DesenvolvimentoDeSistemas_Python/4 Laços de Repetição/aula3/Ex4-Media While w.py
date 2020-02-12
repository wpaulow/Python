# Exemplo 4 - Utilizando o While
nome = input ("Digite o nome do aluno:")
n = 0 #Cria o contador e atribuí 0 de início
qtdnotas = int(input("Digite quantas notas serão utilizadas no cálculo dessa média:"))

total = 0 #Cria um acumulador que vai possuir o total
while qtdnotas > n:
    dig = float(input("Digite a nota do aluno:")) #Recebe a nota
    total = total + dig #recebe o valor atual + a nota
    n += 1 #Acrescenta +1 ao valor de n
media = total / qtdnotas #Calcula a média e atribuí à variável média
if media >= 7:
    status = "Aprovado"
else: status = "Reprovado"

print("A média do %s foi %5.2f, portanto ele está %s!!!" % (nome, media, status))
'''O símbolo de % serve como um espaço reservado às variáveis que serão concatenadas em uma string para ser printada,
facilitando o processo de concatenação. No caso de strings é necessário %s, no caso de int ou double %d, 
e assim sucessivamente'''
