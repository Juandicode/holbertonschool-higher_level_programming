#!/usr/bin/python3
""" a function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """Lee un archivo de texto (UTF-8) y lo imprime en stdout."""

    """ Usamos 'with' para abrir el archivo
    en modo lectura ('r') con codificación UTF-8"""
    with open(filename, "r", encoding="utf-8") as file:
        # Leemos todo el contenido del archivo y lo imprimimos
        # Usamos 'end=""' para evitar agregar una nueva línea extra al final
        print(file.read(), end="")
