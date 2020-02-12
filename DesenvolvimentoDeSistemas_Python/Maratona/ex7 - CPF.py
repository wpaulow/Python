def mascaraCpf(cpf):
    cpf.count('.')
    if cpf.count('.') > 0:
        cpf1 = cpf.split('-')
        cpf1 = "".join(cpf1)
        cpf2 = cpf1.split('.')
        cpf2 = "".join(cpf2)

        '''novoCpf = ''
        for c in cpf2:
            novoCpf += c'''

        print(cpf2)

    elif cpf.count(".") == 0:
        cpfmasc = cpf[0] + cpf[1] + cpf[2]+"."+cpf[3] + cpf[4] + cpf[5] + "." + cpf[6] + cpf[7] + cpf[8] + "-" + cpf[9]\
                  + cpf[10]

        print(cpfmasc)

inpCPF = input("Digite seu cpf com traços e pontos e receba sem eles ou digite sem traços e pontos e receba com eles:")
mascaraCpf(inpCPF)