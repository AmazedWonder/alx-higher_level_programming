#!/usr/bin/python3
"""Defines a Rectangle subclass Square.

defines a class Square that inherits from the Rectangle class.
The Square class represents a square and utilizes the Rectangle class
for its implementation.

The Square class has an __init__ method that takes a size parameter.
Within the __init__ method, the integer_validator method from the
Square class is used to validate the size value. If the value
passes the validation, it is passed as arguments to the
super().__init__ method to initialize the Rectangle superclass
with the width and height set to the size value. The __size
attribute is also assigned with the size value.

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
