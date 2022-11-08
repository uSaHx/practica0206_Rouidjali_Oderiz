nombre = input("Introduzca su nombre: \n")
edad = input("Introduzca su edad: \n")
direccion = input("Introduzca su direccion:\n")
telefono = input("Introduzca su numero de telefono:\n")
datos = {}
datos["nombre"] = nombre
datos["edad"] = edad
datos["direccion"] = direccion
datos["telefono"] = telefono

print("Su nombre es", datos["nombre"], "tiene", datos["edad"], "años, vive en", datos["direccion"],
      "y su numero de telefono es", datos["telefono"], end="")


