#!/usr/bin/python3
"""Defines a class-checking function.

defines a function is_same_class that checks if an object
obj is exactly an instance of a given class a_class.

The function uses type() function to get the type of the obj
and compares it with the a_class using the == operator. If the
types match, it returns True, indicating that the obj is exactly
an instance of a_class. Otherwise, it returns False.

"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
