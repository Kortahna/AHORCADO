#Juego del ahorcado, vas introduciendo letras para adivinar la palabra.

import random
import os, sys
from tkinter import Menu


#En esta funcion hacemos que python no diferencie entre vocales con tilde o sin ellas
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


#En esta función le comentamos al jugador que ha ganado y cerramos el juego
def ganar(eleccion_juego):
    print("\n" + "Efectivamente es " + eleccion_juego + ", ¡HAS GANADO!" + "\U0001F917")
    sys.exit()


#En esta función sustituimo las _ por las letras de la palabra y viceversa
def sustitucion(eleccion_juego, lista_letras):
    print("\n" + ":::::::::::::::::::::::::" + "\n")
    print("Adivina la palabra:" + "\n")
    print("")
    for i in range(0, len(eleccion_juego)):
        if eleccion_juego[i] in lista_letras:
            print(eleccion_juego[i], end=" ")
        else:
            print("_", end=" ")
    print("\n")


# Leo el archivo data y lo convierto en una lista para Python
# Hago que el programa seleccione una palabra de la lista para jugar
def leerarchivo():
    lista_palabras = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as palabras:
        for palabra in palabras:
            lista_palabras.append(palabra.strip())

    eleccion_juego = random.choice(lista_palabras)
    return eleccion_juego


#Aquí definimos el funcionamiento principal del juego, los turnos, la limpieza de pantalla, controlamos los errores principales, etc.
def juego():
    turnos = 5
    eleccion_juego = normalize(leerarchivo())
    lista_letras = []
    os.system("cls")
    # print(eleccion_juego)
    # print(len(eleccion_juego))
    while turnos > 0:
        sustitucion(eleccion_juego,lista_letras)
        letra_elegida = normalize(input("Ingresa una letra: " + "\n" + "\n" + ":::::::::::::::::::::::::" + "\n" + "\n"))
        try:
            if letra_elegida.isnumeric() or letra_elegida == "" or letra_elegida == " ":
                raise ValueError("No se admiten números, ni espacios en blanco o falta de carácteres" + "\n")
            if letra_elegida in lista_letras:
                print("\n" + "Esta letra ya la has usado, prueba con otra" + "\n")
            else:
                lista_letras.append(letra_elegida)
                turnos -= 1
                recorrido = True
                for i in eleccion_juego:
                    if i not in lista_letras:
                        recorrido = False
                        break
                if recorrido:
                    ganar(eleccion_juego)    
                os.system("cls")
        except ValueError as ve:
            print(ve)
    else:
        sustitucion(eleccion_juego,lista_letras)
        respuesta = input("¿De qué palabra se trata?" + "\n")
        if normalize(respuesta.lower()) == eleccion_juego:
            ganar(eleccion_juego)
        else:
            print("\n" + "Oh no! Esa no es la palabra, lo siento, has perdido, la palabra era: " + eleccion_juego)


def run():

    contador = 10

    menu = """
    
    EL JUEGO DEL AHORCADO

    El juego consiste en adivinar la palabra, puedes pedir hasta 5 letras,
    luego tendrás que adivinar la palabra. Si lo consigues ganarás, si no,
    perderás. Pero tranquilo, podrás volver a jugar.

    Empezamos:
    (Presiona cualquier letra y luego enter)
    
    """

    if input(menu):
        juego()   


if __name__ == '__main__':
    run()