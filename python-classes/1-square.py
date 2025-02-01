#!/usr/bin/python3
"""Module that defines a Square class."""  # ← Agregar esta docstring de módulo

class Square:
    """Define a square."""
    
    def __init__(self, size):
        """Initialize a square with a given size.
        
        Args:
            size: The size of the square.
        """
        self.__size = size