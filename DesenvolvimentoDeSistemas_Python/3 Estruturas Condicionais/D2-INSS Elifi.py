print("Bem vindo ao progama que calcula \no seu INSS!")
print("\nTabela para base do calculo:\nSalario até R$ 1693,72 - 8%")
print("Salario maior que R$ 1693,72 e menor que R$ 2822,90 - 9%")
print("Salario maior que R$ 2822,90 - 11%")
salario = float(input("\nDigite seu salário:"))
if salario <= 1693.72:
    PercentDesc = 0.08
elif 1693.72 < salario < 2822.9:
    PercentDesc = 0.09
else:
    PercentDesc = 0.11
ValDesc = salario * PercentDesc
print("O valor descontado do seu salario será R$ %6.2f.\nPois você esta na classe de dedesconto de %5.2f porcento." %(ValDesc, PercentDesc*100))
