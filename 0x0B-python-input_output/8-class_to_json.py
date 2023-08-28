#!/usr/bin/python3
"""Defines a Python class-to-JSON function.

Defines a function called class_to_json that takes an
object as input and returns a dictionary representation
of the object's attributes.

The function utilizes the __dict__ attribute of the object
to access its attribute-value pairs. In Python, the __dict__
attribute is a dictionary that contains the object's attributes
and their corresponding values.

"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
