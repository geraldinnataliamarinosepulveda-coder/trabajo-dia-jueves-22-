"""
Cree una función para precio unitario comparable. Dos paquetes pueden tener tamaños distintos;
no compare solo sus precios totales. Llame para dos paquetes y use los retornos para indicar el más
económico por gramo; si coinciden indique igualdad. Contrato: Precio unitario comparable: recibe
precio total real no negativo en pesos y cantidad real positiva en gramos y devuelve el precio real de un
gramo en pesos.

"""
def precio_unitario_comparable(precio_total, cantidad_gramos):
	"""Devuelve el precio por gramo, en pesos."""
	return precio_total / cantidad_gramos


precio_paquete_1 = precio_unitario_comparable(120, 500)
precio_paquete_2 = precio_unitario_comparable(200, 1000)

if precio_paquete_1 < precio_paquete_2:
	print("El paquete 1 es más económico por gramo.")
elif precio_paquete_2 < precio_paquete_1:
	print("El paquete 2 es más económico por gramo.")
else:
	print("Ambos paquetes tienen el mismo precio por gramo.")