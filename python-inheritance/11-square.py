#!/usr/bin/python3
"""
Defines the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize the square with a given size."""
        self.integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
