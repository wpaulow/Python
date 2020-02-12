def fatorial(nro):
	if nro > 0:

		fatnro = 1
		count = nro
		while count > 0:
			fatnro = fatnro * nro
			count = count -1

		print('%s! = %d' % (nro, fatnro))

	elif (nro == 0):
		print('0! = 1')

	else:
		print('O valor digitado deve ser maior que zero')


fatorial(-5)
fatorial(0)
fatorial(1)
fatorial(3)
fatorial(5)
fatorial(7)

#OK