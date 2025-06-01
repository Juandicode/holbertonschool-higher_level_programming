#!/usr/bin/python3
"""
Module that defines a function to check exact instance type.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
