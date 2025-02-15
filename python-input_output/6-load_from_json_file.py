#!/usr/bin/python3
"""Crea un objeto desde un archivo JSON."""


import json


def load_from_json_file(filename):
    """
    Carga un objeto desde un archivo JSON.

    Args:
        filename (str): El nombre del archivo JSON.

    Returns:
        object: El objeto cargado desde el archivo JSON.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
