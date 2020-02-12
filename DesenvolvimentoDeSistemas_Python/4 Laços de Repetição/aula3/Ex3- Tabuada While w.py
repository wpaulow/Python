#Exemplo 3 - Utilizando o While

x = 0 ''' Define x como 0. Aqui preciso inicializar a variável antes. Diferentemente de outras linguagens onde 
os parâmetros do while são expressos dentro dele mesmo.'''
num1 = int(input("Digite o número da tabuada desejada:")) #Recebe o número
while x<= 10: #Enquanto x for igual ou menor que 10
    result = num1 * x #Resultado recebe o número vezes o valor atual de x
    print ("%d X %d = %d" % (num1, x, result)) #Exibe os valores na tela
    x += 1 #Acrescente +1 ao valor de x

