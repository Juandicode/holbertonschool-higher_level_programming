#!/usr/bin/python3
""" a function that adds two integers or floats after casting them to integers.

The function checks if the inputs are valid numbers (integers or floats), and if not, it raises a TypeError.
It then casts the inputs to integers and returns the sum of the two numbers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast to integers before adding
    return int(a) + int(b)
