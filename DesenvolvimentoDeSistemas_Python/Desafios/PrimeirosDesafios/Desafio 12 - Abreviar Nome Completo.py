# Programa que abrevia nome completo do Fulano, Beltrano ou Ciclano

nomeCompleto = input("Digite seu nome completo, querid@:")

listaNomeSeparado = nomeCompleto.split(" ")

listaNomeAbreviado = (listaNomeSeparado[0], listaNomeSeparado[-1])

nomeAbreviado = " ".join(listaNomeAbreviado)

print("Seu nome abreviado é: ",nomeAbreviado)
print(listaNomeSeparado)
