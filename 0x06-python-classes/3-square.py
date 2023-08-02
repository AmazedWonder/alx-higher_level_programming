#!/usr/bin/python3
"""Define a class Square.

Defines a square with a private instance attribute __size,
validates the size argument using the rules specified in the prompt,
and uses property decorators to define getter and setter methods for
the size attribute, along with a public instance method area that
returns the area of the square.

"""


class Square:
    """A class that represents a square.
       Defining a Square class with a private instance attribute __size

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """__init__,Initializes a new instance of the Square class.
           Defining an __init__ method that takes an optional size
           argument and initializes the __size attribute with it.

        Args:
            size (int, optional): The size of the square.
            Default size set to 0.
        """
        if not isinstance(size, int):
            """validating that it's an integer and greater than or equal to
               zero,and raising an appropriate exception otherwise.
            """

            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square,
           using the instance's __size attribute.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
