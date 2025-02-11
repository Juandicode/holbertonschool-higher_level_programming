#!/usr/bin/python3

""" A function that writes a string to a text file
(UTF8) and returns the number of characters written"""

def write_file(filename="", text=""):


""" Usamos 'with' para abrir el archivo
    en modo escribir (write) ('w') con codificación UTF-8"""
    with open(filename, "w", encoding="utf-8") as file:

        chars_written = file.write(text)  # Escribe el texto en el archivo y obtiene el número de caracteres escritos
    return chars_written  # Devuelve el número de caracteres escritos
