#!/usr/bin/python3

def write_file(filename="", text=""):
    """Escribe un texto en un archivo y devuelve el número de caracteres escritos."""
    
    # Abrimos el archivo en modo de escritura ('w'), lo que crea el archivo si no existe o lo sobrescribe si ya existe
    with open(filename, "w", encoding="utf-8") as file:
        chars_written = file.write(text)  # Escribe el texto en el archivo y obtiene el número de caracteres escritos
    return chars_written  # Devuelve el número de caracteres escritos
