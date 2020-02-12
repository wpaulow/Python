# Exemplo 6 - Utilizando o OR
print("Você quer uma noticia boa ou ruim???")
verifica = (input("Digite B para noticia boa ou R para a ruim: "))
if verifica == "B" or verifica == "b":  # Se a informação digitada for B ou b
    print("Hoje é sexta feira =D ")  # Saida de dados
elif verifica == "R" or verifica == "r":  # Se a informação digitada for R ou r
    print("Você tem lição de casa e trabalhos pra fazer =(")
else:  # Senão
    print("Digite apenas B ou R!!!")
