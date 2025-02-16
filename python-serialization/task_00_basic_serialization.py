#!/usr/bin/python3
"""Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file
 and deserialize the JSON file to recreate the Python Dictionary"""


import json

def serialize_and_save_to_file(data, filename):
    """
    Serializa un diccionario a JSON y lo guarda en un archivo.

    Args:
        data (dict): El diccionario a serializar.
        filename (str): El nombre del archivo donde se guardará el JSON.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Lee un archivo JSON y lo deserializa a un diccionario de Python.

    Args:
        filename (str): El nombre del archivo JSON a leer.

    Returns:
        dict: El diccionario deserializado.
    """
    with open(filename, 'r') as file:
        return json.load(file)
