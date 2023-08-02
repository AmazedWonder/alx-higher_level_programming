#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that represents a square.

    Attributes:
        __size (int): The size of the square(private)
    """

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
