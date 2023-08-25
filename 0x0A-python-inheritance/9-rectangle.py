#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry.

defines a class Rectangle that inherits from BaseGeometry. The
Rectangle class represents a rectangle and utilizes the
BaseGeometry class for validation of width and height values.

The Rectangle class has been modified to use the super() function
to call the integer_validator method from the BaseGeometry class.
This allows the Rectangle class to inherit and reuse the validation
logic defined in BaseGeometry.

The __init__ method takes width and height as parameters, and it
uses super().integer_validator to validate the values. If the
values pass the validation, they are assigned to the private
attributes __width and __height respectively.

The area method calculates and returns the area of the rectangle
by multiplying __width and __height.

The __str__ method provides a string representation of a Rectangle
object. It returns a string that includes the class name and the
width and height values.

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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
