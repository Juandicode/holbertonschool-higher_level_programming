#!/usr/bin/python3
"""
returns True if the object is an instance, or if the object is
an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
   return true if obj is an instance
    of a_class or an instance
    of a class that inherited from a_class.
    sino, return False.
    """
    return isinstance(obj, a_class)
