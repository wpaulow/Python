# Exemplo 3 - Pesquisa in e not in
S = "Maria Amélia Souza"  # Cria a String
print("Amélia" in S)
# Verifica se Amelia está na String, neste caso True
print("Maria" in S)
# Verifica se Maria está na String, neste caso True
print("Souza" in S)
# Verifica se Souza está na String, neste caso True
print("a A" in S)
# Verifica se a A está em alguma parte da String, neste caso True
print("amélia" in S)
# Verifica se amelia está na String, neste caso False por causa da letra minuscula
S = "Todos caminhos levam a Roma"
print("levan" not in S)  # Verifica se levam não está na String, neste caso False
print("Caminhos" not in S)  # Verifica se Caminhos não está na String,
# neste caso True, pois caminhos é diferente de Caminhos
