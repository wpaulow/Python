palavra = input("Digite uma palavra: ")
cont = 0

for letra in palavra:  # para cada letra na palavra
    cont +=1

print("A palavra tem %d letras!" % cont)