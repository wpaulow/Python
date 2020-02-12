from idade import*
print("Digite  sua data de nascimento")
y = int(input("Digite o ano: "))
m = int(input("Digite o mes: "))
d = int(input("Digite o dia: "))
idade = Idade(y,m,d)
print(idade.totalDias())


