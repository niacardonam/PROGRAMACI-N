"""
conjunto = {"carro","casa","beca","empresa"}
conjunto2 = set(("carro","casa","beca","empresa"))
print(conjunto)
print(conjunto2)
"""

frutas ={"manzana","piña","naranja","mandarina"}
carros = {"toyota","bmw","rolls-royce","bmw", "piña"}
print(frutas)
print(carros)
frutas.add("uva")
print(frutas)
#metodo permite aggregar

#conjunto vacio, lo limpia pero sigue existiendo
#frutas.clear()
print(frutas)

copia = frutas.copy()
print(copia)
print(frutas.difference(carros))
frutas.discard("uva")
print(frutas)
