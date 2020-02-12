# Utilizando o For crie um programa que solicita uma palavra para o usuário e então retorna quantas letras ela tem.

palavra = input("Digite uma palavra e saiba o seu número de letras, meu caro usuário:")
cont = 0

for letra in palavra:
    cont += 1

print("A palavra escolhida possuí" , cont , "letras.")

