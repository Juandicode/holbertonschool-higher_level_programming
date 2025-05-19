#!/usr/bin/python3
"""
This module defines the matrix_divided function.
It divides all elements of a matrix by a given number.
"""

def matrix_divided(matrix, div):
"""
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): Matrix of integers/floats.
        div (int or float): The number to divide by.

    Returns:
        list of lists: New matrix with results rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats.
        TypeError: If each row doesn't have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("cada row de la matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
