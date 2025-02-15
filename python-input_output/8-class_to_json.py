#!/usr/bin/python3
""" Write a function that returns the
 dictionary description with simple data structure
 (list, dictionary, string,
 integer and boolean) for JSON serialization of an object"""


def class_to_json(obj):
    """
    Convierte un objeto en un diccionario para serialización JSON.

    Args:
        obj: Una instancia de una clase.

    Returns:
        dict: Un diccionario con los atributos del objeto.
    """
    return obj.__dict__
