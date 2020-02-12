# Exemplo 3 - Utilizando o IF, ELSE e ELIF
nota1 = float(input("Digite a primeira nota:"))  # Recebe a nota 1
nota2 = float(input("Digite a segunda nota:"))  # Recebe a nota 2
media = (nota1 + nota2) / 2  # Calcula a media e atribui à variavel
print("A média do aluno é ", media)  # Escreve a media
if media >= 7:  # Se a média for maior ou igual a 7
    print("Aluno aprovado!")  # Escreve aluno aprovado
elif media < 5:  # SenãoSe a média for menor que 5
    print("Aluno reprovado!")  # Escreve aluno reprovado
else:  # Senão
    print("Aluno de recuperação!")  # Escreve aluno de recuperação
