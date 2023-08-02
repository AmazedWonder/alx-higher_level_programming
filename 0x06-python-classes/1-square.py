#!/usr/bin/python3
"""Define a class Square.

The size of a square is crucial for a square, many things
depend of it (area computation, etc.), so, as class builder,
must control the type and value of this attribute. One way
to have the control is to keep it privately.

self is a conventionally used first parameter name in instance
methods of a class. The self parameter holds a reference to the
instance of the class that the method is being called on. It is
used to access the instance's attributes and methods.

Defines an __init__ method that takes an optional size argument
and initializes the __size attribute with it, after validating that
it's an integer and greater than or equal to zero, and raising an
appropriate exception otherwise.

"""


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
