'''Esse desafio eu não fazia ideia de como fazer. Só fui entender depois que vi o código
do Lucas. Então, como não convém copiar e colar porquê não vale de nada, terei ao menos
o trabalho de comentá-lo, para assim tentar memorizar o passo a passo e ter documentada
essa solução.'''

def cenDezUnid(nro):
	print('Valor digitado: %d' % nro)

	strnro = str(nro) # Aqui é pego o num digitado pelo usuário e transformado em string
	#pois strings são listas de caracteres no python. sendo assim é possível trabalhar
	#com os métodos envolvendo strings nesse numeral.
	if len(strnro) == 3: # len é o método para contar os caracteres de uma string, ou seus campos,
		# já que também se trata de um array
		#sendo assim, se contém 3 campos, é uma centena, e por isso
		if strnro[2] == str(0): # se o terceiro campo [2] é igual à zero, não tem porque dizer 0 unidades
			print('%s centenas, %s dezenas.' %(strnro[0], strnro[1]))
		else: #caso o contrário, "lê-se" cada numeral
			print('%s centenas, %s dezenas, %s unidades.' %(strnro[0], strnro[1], strnro[2]))
	elif len(strnro) == 2:
		if(strnro[1] == str(0)):
			print('%s dezenas' %(strnro[0]))
		else:
			print('%s dezenas, %s unidades' %(strnro[0], strnro[1]))
	elif len(strnro) == 1:
		print('%s unidades' %(strnro[0]))

num = int(input("Digite um número de 0 à 999:"))
cenDezUnid(num)