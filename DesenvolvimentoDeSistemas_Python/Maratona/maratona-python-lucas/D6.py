def cenDezUnid(nro):
	print('Valor digitado: %d' %(nro))

	snro = str(nro)
	if len(snro) == 3:
		if snro[2] == str(0):
			print('%s centenas, %s dezenas' %(snro[0], snro[1]))
		else:
			print('%s centenas, %s dezenas, %s unidades' %(snro[0], snro[1], snro[2]))
	elif len(snro) == 2:
		if(snro[1] == str(0)):
			print('%s dezenas' %(snro[0]))	
		else:
			print('%s dezenas, %s unidades' %(snro[0], snro[1]))
	elif len(snro) == 1:
		print('%s unidades' %(snro[0]))


cenDezUnid(987)
cenDezUnid(780)
cenDezUnid(326)
cenDezUnid(12)
cenDezUnid(3)

#ok