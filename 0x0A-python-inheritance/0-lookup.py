#!/usr/bin/python3
"""Defines an object attribute lookup function.

a function lookup that takes an object as an argument and returns
a list of the object's available attributes using the dir() function.

The dir() function returns a sorted list of strings containing
the names of the object's attributes and methods. It includes
all attributes and methods, including built-in ones, inherited ones,
and those defined specifically for the object.

"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
