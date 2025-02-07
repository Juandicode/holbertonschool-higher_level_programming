#!/usr/bin/python3

from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__width} - {self.__height}"

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height
