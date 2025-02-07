#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry:
    """Class BaseGeometry with an unimplemented area method and integer validation"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
