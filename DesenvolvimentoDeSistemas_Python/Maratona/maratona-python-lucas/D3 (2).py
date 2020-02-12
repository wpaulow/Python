def exibirFrase(frase):
	print('Frase em maiuscula: %s' %(frase.upper()))
	print('Frase em minúscula: %s' %(frase.lower()))
	print('Frase com as primeiras letras capitalizadas: %s' %(frase.title()))

	vogais = 0
	consoantes = 0

	for letra in frase:
		if letra == 'A' or letra == 'a':
			vogais += 1
		elif letra == 'E' or letra == 'e':
			vogais += 1
		elif letra == 'I' or letra == 'i':
			vogais += 1
		elif letra == 'O' or letra == 'o':
			vogais += 1
		elif letra == 'U' or letra == 'u':
			vogais += 1
		elif letra != ' ':
			consoantes += 1
		
	print('Vogais: %d' %(vogais))
	print('Consoantes: %d' %(consoantes))



exibirFrase("O rato roeu a roupa do rei de Roma")
#OK