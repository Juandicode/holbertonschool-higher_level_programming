#!/usr/bin/python3
"""modulo q define una clase cuadrado."""


class Square:
    """defino un cuadrado."""

    def __init__(self, size=0):
        """Inicializa un cuadrado con un tamaño dado.

        Args:
        size (int): El tamaño del cuadrado. Debe ser un número entero >= 0.

        Raises:
        TypeError: Si size no es un número entero.
        ValueError: Si size es menor que 0."""

        if not isinstance(size, int):
            raise TypeError("size tiene que ser un integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
