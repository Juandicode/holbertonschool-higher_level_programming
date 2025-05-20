#!/usr/bin/python3
"""modulo q define la clase cuaudrado."""


class Square:
    """la class square define un cuadrado."""

    def __init__(self, size=0):
        """inicializo un cuadrado con un tamaño.

        Args:
            size: el tamaño de la clase."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
