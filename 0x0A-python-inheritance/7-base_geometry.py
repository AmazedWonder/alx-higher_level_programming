#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry.

defines a class BaseGeometry that represents the base geometry.

The class includes two methods:

area(self): This method raises an exception with a message
indicating that the area() method is not implemented. It serves as
a placeholder to indicate that subclasses should provide their own
implementation of the area() method.

integer_validator(self, name, value): This method is used to
validate a parameter value as an integer. It takes two arguments:
name (the name of the parameter) and value (the parameter to validate).
If the value is not an integer or is less than or equal to 0, it
raises a TypeError or ValueError respectively, with an appropriate
error message.

"""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
