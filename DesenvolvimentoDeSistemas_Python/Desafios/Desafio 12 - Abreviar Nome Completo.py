# Programa que abrevia nome completo do Fulano, Beltrano ou Ciclano

nomeCompleto = input("Digite seu nome completo, querid@:")

listaNomeSeparado = nomeCompleto.split(" ")

listaNomeAbreviado = (listaNomeSeparado[0], listaNomeSeparado[-1])

print(listaNomeAbreviado)

nomeAbreviado = " ".join(listaNomeAbreviado)

print(nomeAbreviado)
