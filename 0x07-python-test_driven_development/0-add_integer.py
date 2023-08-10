#!/usr/bin/python3
# 0-add_integer.py
"""Defines add_integer function, a function that
   takes two arguments, a and b, and performs addition on them.
"""


def add_integer(a, b=98):
    """Return: int addtion of a and b.
       Floats args are typecasted into ints before addition.
       Raises:
           TypeError: If either a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
