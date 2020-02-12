# Exemplo  4 - Convertendo Tipos

num1 = int(input ("Digite um número:")) # Recebe o valor e converte para int
num2 = int(input ("Digite um número:"))
soma = num1 + num2
print ("A soma dos dois números é ", soma)
print ("%d + %d = %d" % (num1, num2, soma))

'''OBS: Podemos utilizar % para facilitar o nosso print, podendo marcar a posilção
onde aparecerá a variável, substituindo isto:
print (num1, "+", num2, "=", soma)
Por isso:
print ("%d + %d = %d" % (num1, num2, soma))
%d ou %i para os inteiros, %f para o float, %s para string e assim vai...
'''
