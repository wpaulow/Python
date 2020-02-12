# Exemplo 5 - Utilizando o While True
nome = input("Digite o nome do aluno:")  # Recebe o Nome
n = 0  # Cria um contador e atribui 0 a ele
total = 0  # Cria um acumulador que vai possuir o total
while True:  # Enquanto verdadeiro - loop infinito
        dig = input("Digite a nota do aluno ou fim para encerrar:")  # Recebe a nota ou fim
        if dig.upper() == "FIM":  # Compara se o valor digitado convertido em miusculo é FIM
                break  # Encerra o while
        total = total+float(dig)  # total recebe seu atual valor + a nota digitada
        n += 1  # Acrescenta +1 ao valor de n
media = total / n  # Calcula a media e atribui à variavel
if media >= 7:  # Se a média for maior ou igual a 7
        status = "aprovado"  # Status recebe aprovado
else:  # Senão
        status = "reprovado"  # Status recebe reprovado
print("A média do %s foi %5.2f, portanto ele está %s!!!" % (nome, media, status))
# Escreve a média, e se está ou não aprovado
