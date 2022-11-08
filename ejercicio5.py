diccionario = {}
palabra = []

while True:
    usr_palabra = input("Introduzca la palabara y su traduccion separados por dos puntos "
                     "puede parar el programa con [Terminar]: \n")
    if usr_palabra == "Terminar":
        break
    palabra = usr_palabra.split(":")
    diccionario[palabra[0]] = palabra[1]
    print(palabra)
frase = input("Introduzca una frase en Español para traducir al Ingles")

