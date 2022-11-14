base_datos = [{"01":{"dsa":"sads", "sa":"lk"},
               "02":{"ads":"True"}}]

print("--------------------------------------------")
print("            Seleccione una opcion:          ")
print("--------------------------------------------")
print("         [1] Nuevo alumno")
print("         [2] Eliminar Alumno")
print("         [3] Mostrar Alumno")
print("         [4] Mostrar Base de Datos")
print("         [5] Mostrar Lista de Aprobados")
print("         [6] Termninar Programa")
print("--------------------------------------------")

while True:
    opcion = int(input("Seleccione una opcion: \n"))
    if opcion == 1:
        nif = input("DNI del nuevo alumno:\n")
        nombre = input("Nombre del nuevo alumno:\n")
        apellidos = input("Apellidos del nuevo alumno: \n")
        telefono = input("Numero de telefono del nuevo alumno: \n")
        correo = input("Correo del nuevo alumno: \n")
        aprobado = input("¿Ha aprobado el nuevo alumno?: True o False \n")
        datos = {}
        datos["nombre"] = nombre
        datos["apellidos"] = apellidos
        datos["telefono"] = telefono
        datos["correo"] = correo
        datos["aprobado"] = aprobado
        dic_nif = {}
        dic_nif[nif] = datos
        base_datos.append(dic_nif)
        print(base_datos)
    elif opcion == 2:
        x2 = input("NIF del Alumno que desea eleminar: \n")
        for i in base_datos:
            del i[x2]
        print(base_datos)
    elif opcion == 3:
        x3 = input("NIF del Alumno que desea visualizar: \n")
        for i in base_datos:
            print(i[x3])
    elif opcion == 4:
        for i in base_datos:
            print(i)
    elif opcion == 5:
        for i in base_datos:
            if "True" in i:
                print(i)
            else:
                print("No hay aprobados")
    elif opcion == 6:
        break
