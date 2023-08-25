#!/usr/bin/python3
"""Defines an inherited class-checking function.

defines a function inherits_from that checks if an object
obj is an inherited instance of a given class a_class.

The function first uses the type() function to get the type of obj.
Then, it checks if the type of obj is a subclass of a_class using
the issubclass() function. Additionally, it checks if the type of
obj is not equal to a_class to exclude cases where obj is an exact
instance of a_class.

If obj is an inherited instance of a_class, the function returns
True. Otherwise, it returns False.

"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
