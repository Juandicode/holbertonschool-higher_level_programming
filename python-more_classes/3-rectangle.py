#!/usr/bin/python3
"""Defines a Rectangle class with string representation."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """inicializo nuevo rectangulo .

        Args:
            width (int): ancho del rectang.
            height (int): largo del rect.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set del ancho  del Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set alto del  rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)
