usuarios=[]

while True:
    nombre = input("digita un nombre o x:")
    
    if nombre == "x":
        break

    usuarios.append(nombre)
print("usuarios registrados:", usuarios)


#tiene varios nombres repetidos
nombre1 = {"diego","camila","luisa","raul"}
nombre2 = {"diego","camila","cesar","david"}
print(nombre1.intersection(nombre2))
nombre3 = {"hhh"}
nombre3 = {"hhh"}