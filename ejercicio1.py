divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa_intr = str.capitalize(input("Introduzca el nombre de la divisa: \n"))

if divisa_intr in divisas:
    print("El simbolo de la divisa que ha introducido es:", divisas.get(divisa_intr))
else:
    print("El nombre de la divisa no esta en la base de datos")