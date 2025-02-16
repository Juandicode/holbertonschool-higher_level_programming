#!/usr/bin/python3
"""
A class that defines a student by first_name, last_name, and age.
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings representing the
            attributes to include.
                          If None, all attributes are included.

        Returns:
            dict: A dictionary containing the specified
            attributes of the student.
        """
        if attrs is None:
            # Return all attributes
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            # Return only the specified attributes that exist in the instance
            resultado = {}
            for key in attrs:
                if hasattr(self, key):
                    resultado[key] = getattr(self, key)
            return resultado
