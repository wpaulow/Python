def calcularTrapezio(bMenor, bMaior, altura):
	return float(float((bMaior + bMenor) * altura) / 2.0)


b = float(input('Forneça a base menor do trapézio: '))
B = float(input('Forneça a base maior do trapézio: '))
h = float(input('Forneça a altura do trapézio:'))

print('Área do trapézio: %.1f' %(calcularTrapezio(b, B, h)))
print('')
print('Área do trapézio: %.1f' %(calcularTrapezio(5, 10, 6)))
print('Área do trapézio: %.1f' %(calcularTrapezio(20, 35, 15)))
print('Área do trapézio: %.1f' %(calcularTrapezio(46, 75, 33)))

#ok