"""
Caso. Cree una función para pago semanal con horas extra. Es un modelo ficticio: las primeras 40 horas
se pagan a la tarifa ordinaria; solo las horas que exceden 40 se pagan a 1,5 veces esa tarifa. Llame para
dos personas y sume los retornos, sin redondearlos antes de sumar. Contrato: Pago semanal con horas
extra: recibe horas semanales reales no negativas y tarifa real no negativa en pesos por hora y devuelve
el pago real semanal en pesos.

"""
def pago_semanal(horas, tarifa):
	"""Devuelve el pago semanal, con horas extra a 1,5 veces la tarifa."""
	horas_ordinarias = min(horas, 40)
	horas_extra = max(horas - 40, 0)
	return horas_ordinarias * tarifa + horas_extra * tarifa * 1.5


horas_persona_1 = float(input("Horas trabajadas por la persona 1: "))
tarifa_persona_1 = float(input("Tarifa por hora de la persona 1: "))
horas_persona_2 = float(input("Horas trabajadas por la persona 2: "))
tarifa_persona_2 = float(input("Tarifa por hora de la persona 2: "))

total = pago_semanal(horas_persona_1, tarifa_persona_1) + pago_semanal(
	horas_persona_2, tarifa_persona_2
)
print("Pago total:", total)