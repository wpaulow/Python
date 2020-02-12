# Exemplo 4 - find e rfind
s = "Alo Mundo"
print(s.find("Mun"))
''' Pesquisa Mun na String, e retorna o indice do primeiro
caractere encontrado, nesse caso 4'''
print(s.find("OK"))
# Pesquisa OK na String, retorna -1, pois não enontrou
print("="*100)
t = "Um dia de sol"
print(t.find("d"))
# Pesquisa d da esquerda para direita, portanto retorna 3
print(t.rfind("d"))
# Pesquisa da direita para a esquerda, portanto retorna 7
