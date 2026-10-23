"""
Caso. Cree las funciones necesarias para descuento seguido de impuesto ficticio. El descuento se calcula
sobre la base. El impuesto se calcula sobre el subtotal ya descontado, no sobre la base original. Son
reglas ficticias, no normas tributarias. El escenario pasa el retorno del descuento a la función de
impuesto y muestra subtotal y total. Contratos en orden de parámetros: Subtotal descontado: recibe
base real no negativa en pesos, descuento real de 0 a 100 por ciento y devuelve real no negativo en
pesos. Total con impuesto: recibe subtotal real no negativo en pesos, impuesto real no negativo por
ciento y devuelve real no negativo en pesos.
"""

def subtotal_descontado(base, descuento):
	"""Devuelve la base después de aplicar un descuento porcentual."""
	if base < 0:
		raise ValueError("La base debe ser no negativa.")
	if not 0 <= descuento <= 100:
		raise ValueError("El descuento debe estar entre 0 y 100.")
	return base * (1 - descuento / 100)


def total_con_impuesto(subtotal, impuesto):
	"""Aplica un impuesto porcentual al subtotal ya descontado."""
	if subtotal < 0:
		raise ValueError("El subtotal debe ser no negativo.")
	if impuesto < 0:
		raise ValueError("El impuesto debe ser no negativo.")
	return subtotal * (1 + impuesto / 100)


def escenario(base, descuento, impuesto):
	"""Calcula e imprime el subtotal descontado y el total con impuesto."""
	subtotal = subtotal_descontado(base, descuento)
	total = total_con_impuesto(subtotal, impuesto)
	print(f"Subtotal descontado: ${subtotal:.2f}")
	print(f"Total con impuesto: ${total:.2f}")
	return subtotal, total