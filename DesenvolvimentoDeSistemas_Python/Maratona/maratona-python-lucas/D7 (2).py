def mascaraCpf(cpf):
	print(cpf.count('.'))
	if cpf.count('.') > 0:
		cpf1 = cpf.split('.')
		cpf2 = cpf.split('-')

		novoCpf = ''
		for c in cpf1:
			novoCpf += c

		print(novoCpf)



print(mascaraCpf('487.551.518-92'))