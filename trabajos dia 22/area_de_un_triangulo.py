"""

Caso. Cree una función para área de un triángulo por base y altura. La altura es perpendicular a la base.
Use dos llamadas y muestre las dos áreas y su suma, calculada con los retornos. Contrato: Área de un
triángulo por base y altura: recibe base y altura, reales positivos expresados en centímetros y devuelve
el área real en centímetros cuadrados.

"""
def area_triangulo(base, altura):
	"""Devuelve el área en cm² para una base y altura en centímetros."""
	return base * altura / 2


area1 = area_triangulo(10, 5)
area2 = area_triangulo(8, 4)

print("Área del primer triángulo:", area1, "cm²")
print("Área del segundo triángulo:", area2, "cm²")
print("Suma de las áreas:", area1 + area2, "cm²")