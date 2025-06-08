#!/usr/bin/python3
"""Script que añade argumentos a una lista y los guarda en un archivo JSON."""

import sys
from os import path

# Importar las funciones de los ejercicios anteriores
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Nombre del archivo JSON
filename = "add_item.json"

# Cargar la lista existente o crear una nueva si el archivo no existe
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Añadir los argumentos del script a la lista
my_list.extend(sys.argv[1:])

# Guardar la lista actualizada en el archivo JSON
