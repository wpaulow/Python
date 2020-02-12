def verificarTriangulo(l1, l2, l3):
	triangulo = ''
	if l1 == l2 and l2 == l3:
		triangulo = 'É equilatero'
	elif l1 != l2 and l2 != l3:
		triangulo = 'É escaleno'
	elif (l1 == l2 and l2 != l3 and l1 != l3) or (l1 == l3 and l2 != l1 and l2 != l3) or (l3 == l1 and l1 != l2 and l1 != l3):
		triangulo = 'É isoceles '
	else:
		triangulo = 'Não é triângulo'

	return triangulo


print('Este triangulo: %s' %(verificarTriangulo(15,15,15)))
print('Este triangulo: %s' %(verificarTriangulo(10,10,12)))
print('Este triangulo: %s' %(verificarTriangulo(3,4,5)))
print('Este triangulo: %s' %(verificarTriangulo(5,7,15)))
print('Este triangulo: %s' %(verificarTriangulo(8,8,20)))