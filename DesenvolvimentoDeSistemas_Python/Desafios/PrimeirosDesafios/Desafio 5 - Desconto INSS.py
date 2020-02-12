#Programa que solicita ao usuário o seu salário para então calcular o seu desconto do INSS.

salario = float(input("Digite seu salário para saber o percentual e o valor que é descontado para previdência:"))
desc1 = 0.92
desc2 = 0.91
desc3 = 0.89

if salario <= 1693.72:
    print("Seu desconto é de 8 per 100 de seu salário. Logo, lhe é descontado R$" , salario - salario * desc1 ,
          ". Lhe restando a quantia líquida de R$" , salario * desc1)

elif salario < 2822.90:
    print("Seu desconto é de 9 per 100 de seu salário. Logo, lhe é descontado R$" , salario - salario * desc2 ,
          ". Lhe restando a quantia líquida de R$" , salario * desc2)

else:
    print("Seu desconto é de 11 per 100 de seu salário. Logo, lhe é descontado R$" , salario - salario * desc3 ,
          ". Lhe restando a quantia líquida de R$" , salario * desc3)