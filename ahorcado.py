#Juego del ahorcado, vas introduciendo letras para adivinar la palabra.

import random
import os, sys
from tkinter import Menu


def juego():
    vidas = 5
    eleccion_juego = leerarchivo()
    os.system("cls")
    print("Adivina la palabra" + "\n")
    for i in range(1, len(eleccion_juego)):
        print("_", end=" ")
    print("\n")
    letra_elegida = input("Ingresa una letra: ")
    
    for a in eleccion_juego:
        if a == letra_elegida:
            os.system("cls")
            vidas = vidas - 1
    if vidas == 0:
        respuesta = input("¿De qué palabra se trata?")
        if respuesta == eleccion_juego:
            print("Efectivamente, ¡HAS GANADO!")
        else:
            print("Oh no! Esa no es la palabra, lo siento, prueba de nuevo")   


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
    (Presiona cualquier letra o pulsa enter para continuar)
    
    """

    if input(menu):
        juego()
        


if __name__ == '__main__':
    run()