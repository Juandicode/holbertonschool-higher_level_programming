#!/usr/bin/python3
"""Este módulo contiene la función write_file que escribe
un texto en un archivo y devuelve el número de caracteres escritos."""


def write_file(filename="", text=""):
    """Escribe un texto en un archivo y
    devuelve el número de caracteres escritos."""

    """ Abrimos el archivo en modo de escritura ('w'),|
    lo que crea el archivo si no existe o lo sobrescribe si ya existe"""
    with open(filename, "w", encoding="utf-8") as file:
        chars_written = file.write(text)
        # Escrib en el archiv obtien el núm de caract scritos
    return chars_written  # Devuelve el número de caracteres escritos
