"""
Caso. Cree las funciones necesarias para tolerancia de una medición. Debe reutilizar una función de
valor absoluto que recibe un real y devuelve su distancia al cero. Los extremos de tolerancia se aceptan.
La función de aceptación utiliza el retorno de valor absoluto. El escenario consulta dos mediciones por
separado. Contratos en orden de parámetros: Valor absoluto: recibe real finito y devuelve real no
negativo. Aceptación: recibe medición y objetivo reales, tolerancia real no negativa y devuelve lógico.
Fórmula o relación: Error = valor absoluto de (medición − objetivo); aceptable cuando error ≤
tolerancia.

"""
import math


def valor_absoluto(valor: float) -> float:
	"""Devuelve la distancia de un real finito al cero."""
	if not math.isfinite(valor):
		raise ValueError("El valor debe ser finito.")
	return abs(valor)


def aceptacion(medicion: float, objetivo: float, tolerancia: float) -> bool:
	"""Indica si la medición está dentro de la tolerancia, incluidos sus extremos."""
	if not all(math.isfinite(x) for x in (medicion, objetivo, tolerancia)):
		raise ValueError("Los valores deben ser finitos.")
	if tolerancia < 0:
		raise ValueError("La tolerancia debe ser no negativa.")
	error = valor_absoluto(medicion - objetivo)
	return error <= tolerancia


def main() -> None:
	objetivo = float(input("Objetivo: "))
	tolerancia = float(input("Tolerancia: "))
	for numero in (1, 2):
		medicion = float(input(f"Medición {numero}: "))
		resultado = aceptacion(medicion, objetivo, tolerancia)
		print("Aceptada" if resultado else "Rechazada")


if __name__ == "__main__":
	main()
