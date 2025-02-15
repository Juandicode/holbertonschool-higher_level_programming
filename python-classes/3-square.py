#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Initialize a square con un tamaño.

        Args:
            size (int): The size del cuadrado. debe ser un integer >= 0.

        Raises:
            TypeError: If size no es un integer.
            ValueError: If size es menos que 0."""
        if not isinstance(size, int):
            raise TypeError("size tiene q ser un integer")
        if size < 0:
            raise ValueError("size dbe ser >= 0")
        self.__size = size

    def area(self):
        """retorna el area actualdl cuadrado."""
        return self.__size ** 2
