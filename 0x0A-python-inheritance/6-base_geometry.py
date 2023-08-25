#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry.

defines a class BaseGeometry that represents the base geometry.

The class includes a method area(self) that raises an exception
with a message indicating that the area() method is not implemented.
This serves as a placeholder to indicate that subclasses should
provide their own implementation of the area() method.

Raising an exception, it notifies the user that attempting to
call area() on an instance of the BaseGeometry class will result
in an error unless it is overridden in a derived class.

"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
