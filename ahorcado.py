#Juego del ahorcado, vas introduciendo letras para adivinar la palabra.

import random
import os, sys
from tkinter import Menu

def sustitucion(eleccion_juego, lista_letras):
    print("\n" + "Adivina la palabra" + "\n")
    for i in range(0, len(eleccion_juego)):
        if eleccion_juego[i] in lista_letras:
            print(eleccion_juego[i], end=" ")
        else:
            print("_", end=" ")
    print("\n")


def juego():
    vidas = 5
    eleccion_juego = leerarchivo()
    lista_letras = []
    os.system("cls")
    print(eleccion_juego)
    # print(len(eleccion_juego))
    while vidas > 0:
        sustitucion(eleccion_juego,lista_letras)
        letra_elegida = input("Ingresa una letra: " + "\n")
        lista_letras.append(letra_elegida)
        vidas -= 1
        os.system("cls")
    else:
        sustitucion(eleccion_juego,lista_letras)
        respuesta = input("¿De qué palabra se trata?" + "\n")
        if respuesta.lower() == eleccion_juego:
            print("\n" + "Efectivamente, ¡HAS GANADO!")
        else:
            print("\n" + "Oh no! Esa no es la palabra, lo siento, has perdido")    


# Leo el archivo data y lo convierto en una lista para Python
# Hago que el programa seleccione una palabra de la lista para jugar
def leerarchivo():
    lista_palabras = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as palabras:
        for palabra in palabras:
            lista_palabras.append(palabra.strip())

    eleccion_juego = random.choice(lista_palabras)
    return eleccion_juego


def run():

    menu = """
    
    EL JUEGO DEL AHORCADO

    El juego consiste en adivinar la palabra, puedes pedir hasta 5 letras,
    luego tendrás que adivinar la palabra. Si lo consigues ganarás, si no,
    perderás. Pero tranquilo, podrás volver a jugar.

    Empezamos:
    (Presiona cualquier letra)
    
    """

    if input(menu):
        juego()
        


if __name__ == '__main__':
    run()