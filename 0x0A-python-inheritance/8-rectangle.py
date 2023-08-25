#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry.

defines a class Rectangle that inherits from BaseGeometry.
The Rectangle class represents a rectangle and utilizes the
BaseGeometry class for validation of width and height values.

The Rectangle class has an __init__ method that takes width
and height as parameters. Within the __init__ method, the
integer_validator method from the BaseGeometry class is used to
validate the width and height values. If the values pass the
validation, they are assigned to the private attributes
__width and __height respectively.

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
