
#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from BaseGeometry.
"""


class BaseGeometry:
    """Base class with basic geometric validations."""
    
    def integer_validator(self, name, value):
        """Validate that 'value' is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):  # <--- HERENCIA CORRECTA
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
