# Exemplo 6 - Split e Join
nomeCompleto = "Pedro Henrique Oliveira Mendes"  # Cria a string
listaNomeSeparado = nomeCompleto.split(" ")  # Quebra a String
# separando com base no espaço, criando os elementos da lista
print(listaNomeSeparado[0])  # Imprime o 1º Elemento da lista
print(listaNomeSeparado[1])  # Imprime o 2º Elemento da list
print(listaNomeSeparado[2])  # Imprime o 3º Elemento da list
print(listaNomeSeparado[3])  # Imprime o 4º Elemento da list
listaNomeAbreviado = (listaNomeSeparado[0], listaNomeSeparado[-1])
# adiciona o primeiro e o o ultimo elemento em uma nova lista
print(listaNomeAbreviado)  # Imprime a lista
nomeAbreviado = " ".join(listaNomeAbreviado)  # Tranasforma a
# lista em String adicionando um espaço entre os itens
print(nomeAbreviado)  # Imprime a string
