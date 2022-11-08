datos = {}

while True:
    x = input("Introduzca el tipo de dato que introducira despues "
              "o puede parar el programa introduciendo [Fin] "":\n")
    if x == "Fin":
        break
    y = input("Introduzca el dato:\n")
    datos[x] = y
    print(datos)