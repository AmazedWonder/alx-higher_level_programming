#!/usr/bin/python3
"""Define a class Square.

Defines a square with a private instance attribute __size,
validates the size argument using the rules specified in the
prompt, uses property decorators to define getter and setter
methods for the size attribute, private instance attribute
__position, validates the position argument using the rules
specified in the prompt, uses property decorators to define
getter and setter methods for the position attribute, along
with public instance methods area and my_print.

"""


class Square:
    """Defines a class that represents a square,
       with a private instance attribute __size.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.
           Takes an optional size argument and initializes the
           size attribute with it using the property setter.

        Args:
            size (int, optional): The size of the square.
            Defaults size to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
