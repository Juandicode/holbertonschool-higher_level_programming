#!/usr/bin/python3
"""modulo q define la clase cuaudrado."""


class Square:
    """la class square define un cuadrado."""

    def __init__(self, size=0):
        """inicializo un cuadrado con un tamaño.

        Args:
            size: el tamaño de la clase."""
        self.size = size
        
        
    @property
    def size(self):
        """getter del tamaño."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter para establecer el tamaño del cuadrado con validaciones."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ devuelve el area del cuadrado."""
        return self.__size ** 2
