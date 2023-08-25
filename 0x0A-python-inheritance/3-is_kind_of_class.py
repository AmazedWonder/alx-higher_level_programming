#!/usr/bin/python3
"""Defines a class and inherited class-checking function.

defines a function is_kind_of_class that checks if an object
obj is an instance or inherited instance of a given class a_class.

The function uses the isinstance() function to determine if obj
is an instance of a_class or any class that inherits from a_class.
If obj is an instance or inherited instance of a_class, it returns True.
Otherwise, it returns False.

"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
