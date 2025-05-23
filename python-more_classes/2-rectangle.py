#!/usr/bin/python3
"""Defines an empty Rectangle class."""


class Rectangle:
    """Empty representation of a rectangle."""
    def __init__(self, width)
        """inicializo un rectangulo

        argumentos: 
            width: el ancho de la clase"""
        self.__width = width
    
    @property
    def width(self):
        """getter del tamaño."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter para establecer el tamaño del cuadrado con validaciones."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

