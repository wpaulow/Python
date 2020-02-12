def fatorial(nro):
	if nro > 0:

		fatnro = 1
		count = nro
		while count > 0:
			fatnro = fatnro * count #Lucas havia deixado fatnro = fatnro * nro. mas o nro não se alterava a cada rodada do for. o count, que é baseado no nro informado pelo usuário, estava mudando a cada hora
			count = count -1

		print('%s! = %d' % (nro, fatnro))

	elif (nro == 0):
		print('0! = 1')

	else:
		print('O valor digitado deve ser maior que zero.')


n = int(input("Digite um número:"))
print(fatorial(n))

fatorial(-5)
fatorial(0)
fatorial(1)
fatorial(3)
fatorial(5)
fatorial(7)

#OK