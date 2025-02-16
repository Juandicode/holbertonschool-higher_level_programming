#!/usr/bin/python3
"""class Student that defines a student by """


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Inicializa una instancia de Student con first_name, last_name y age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Devuelve un diccionario con los atributos del estudiante.
        Si se pasa una lista de atributos (attrs), solo se incluyen esos.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }

    def reload_from_json(self, json):
        """
        Actualiza los atributos del estudiante usando un diccionario.
        """
        for key, value in json.items():
            setattr(self, key, value)
