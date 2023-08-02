#!/usr/bin/python3
class Square:
    """A class that represents a square.

    Attributes:
        __size (int): This is size of the square.
        size is private.
    """

    def __init__(self, size=0):
        """__init__,Initializes a new instance of the Square class.

           self is a conventionally used first parameter name in instance
           methods of a class. The self parameter holds a reference to the
           instance of the class that the method is being called on. It is
           used to access the instance's attributes and methods.

        Args:
            size (int, optional): The size of the square.
            Default size is set to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
