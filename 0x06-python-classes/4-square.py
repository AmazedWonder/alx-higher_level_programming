#!/usr/bin/python3
class Square:
    """Defines a Square class with a private instance
       attribute __size.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.
           Defines an __init__ method that takes an optional size
           argument and initializes the size attribute with it using
           the property setter.

        Args:
            size (int, optional): The size of the square.
            Defaults size to 0.
        """
        self.size = size

    @property
    def size(self):
        """Defines a size property with getter and setter methods.
           Getter retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter sets the size of the square.

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
