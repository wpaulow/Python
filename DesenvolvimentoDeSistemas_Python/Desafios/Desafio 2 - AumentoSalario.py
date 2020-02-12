#Desafio 2 - Aumentar percentualmente um salário e retornar o novo salário e o valor que foi aumentado

salario = float(input("Insira o salário que deseja calcular um aumento:"))
percentualAumento = float(input("Insira a porcentagem de aumento que incidirá sobre o salário:"))
salarioNovo = salario * (1+percentualAumento/100)
print("O salário acrescido do percentual de aumento de " , percentualAumento , " é de " , salarioNovo)
print ("O salário acrescido de %5.2f porcento é de R$ %5.2f" %(percentualAumento , salarioNovo))
print ("E o valor correspondente ao aumento é de R$ " , salarioNovo - salario)
sair = input("Digite X para fechar o programa: ")

'''1. Se o usuário digitar o valor correspondente ao salário no formato em que estamos mais acostumados, a saber,
separando a milhar por um ponto, seguido de vírgula depois da unidade para representar os centavos, como corrigir o 
erro?
2. O %5.2f é para limitar o número de casas em 5 antes do ponto e 2 depois dele na saída de dados, no print. 
E para fazer o tratamento com relação aos inputs? Como proceder?
3. No momento de exibir na tela uma mensagem, utilizando o recurso de 'marcação da variável' através do caractere %,
é perdida a possibilidade de usá-lo como uma mera string? Ele se torna um caracter reservado? Um exemplo seria se, caso
eu quisesse printar 'O salário acrescido de %5.2f % é de R$ %5.2f' com o sinal de % depois de %5.2f e antes de 'é de...'
justamente para representar a porcentagem na tela ao usuário eu seria obrigado a escrever porcento ou pontos 
percentuais? 
4. Executando o programa no prompt de comando, fora do PyCharm, se não inserir um input no final, ele roda em um 
segundo e desaparece. Qual o comando que posso usar para que o programa continue na tela? '''