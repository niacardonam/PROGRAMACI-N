frutas = tuple(("fresa","manzana","papaya","manzana" ))
print(frutas)
frutas2 = ("fresa","manzana","papaya","manzana" )
print(frutas2)
print(frutas.count("manzana"))
print(frutas.index("manzana"))

temporal = list(frutas)
print(temporal)
temporal.append("mango")
print(temporal)
frutas=tuple(temporal)
print(frutas)


