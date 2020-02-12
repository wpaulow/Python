def calculadora(n1, n2, operacao):
	con = True
	if operacao == 1:
		print('O resultado é: %d' % (n1 + n2))
	elif operacao == 2:
		print('O resultado é: %d' %(n1 - n2))
	elif operacao == 3:
		print('O resultado é: %d' %(n1 * n2))
	elif operacao == 4:
		print(' O resultado é: %d' %(n1 / 2))

	return con




retorno = True

while retorno:
	operacao = int(input('Selecione a operação: \n 1 - Soma \n '
						 '2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n 5 - Sair  '))
	if operacao == 5:
		retorno = False
	else:
		n1 = int(input('Digite o primeiro valor:  '))
		n2 = int(input('Digite o segundo valor:  '))
		retorno = calculadora(n1, n2, operacao)
		


#Ok