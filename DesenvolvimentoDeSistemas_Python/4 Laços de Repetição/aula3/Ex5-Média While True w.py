nome = input ("Digite o nome do aluno:")
n = 0 #Cria o contador e atribuí 0 de início
total = 0 #Cria um acumulador que vai possuir o total

while True: #Enquanto verdadeiro - loop infinito
    dig = input ("Digite a nota do aluno ou fim para encerrar:") #recebe a nota ou fim
    if dig.upper() == "FIM": #Compara se o valor digitado convertido em maiúsculo é FIM
        break #caso seja fim, já encerra por aqui, se não continua a receber notas
    total = total+float(dig) #total recebe seu atual valor  + a nota digitada
    n+=1
media = total / n

if media >= 7:
    status = "Aprovado"
else: status = "Reprovado"

print("A média do %s foi %5.2f, portanto ele está %s!!!" % (nome, media, status))
