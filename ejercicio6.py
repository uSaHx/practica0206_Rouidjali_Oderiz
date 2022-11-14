base_datos = []

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
if int(input()) == 1:
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
elif int(input()) == 2:
    x = input("NIF del Alumno que desea eleminar: \n")
    base_datos.remove(x)
