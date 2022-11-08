tabla_articulos = {"Pan": 1.40,
                   "Huevos": 2.30,
                   "Cebolla": 0.85,
                   "Aceite": 4.35}
articulo = str.capitalize(input("Introduzca el articulo que desea: \n"))
cantidad = float(input("Introduca la cantidad que desea: \n"))

if articulo in tabla_articulos:
    print("El total de la compra es de:",
    tabla_articulos[articulo] * cantidad, "€", end="")
else:
    print("El producto que ha introducido no esta registrado")