#!/usr/bin/python3
class Square:
    """A class that represents a square.

    Attributes:
        __size (int): The size of the square.
        size here is private.

        Why size is private attribute?

        The size of a square is crucial for a square,
        many things depend of it (area computation, etc.),
        so as class builder, must control the type and value of this
        attribute. One way to have the control is to keep it privately.
    """

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
