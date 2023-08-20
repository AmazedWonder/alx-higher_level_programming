#!/usr/bin/python3
"""Define a class Square that represents square.

The Square class has an __init__ method that is called when
a new instance of the class is created. It initializes the
square with a given size and position.

The size property allows getting and setting the size of the square.
It includes type-checking to ensure that the size is an integer and
value-checking to ensure that it is non-negative. The position property
allows getting and setting the position of the square. It performs various
checks to ensure that the position is a tuple of two positive integers.

The area method calculates and returns the area of the square by
multiplying its size by itself.

The my_print method prints the square using the '#' character. It checks
if the size of the square is 0, in which case it prints an empty line.
Otherwise, it uses nested loops to print the appropriate number of spaces
and '#' characters to represent the square.

The __str__ method defines the string representation of the Square object.
It is called when the object is passed to the print function or when str()
is called on the object.

"""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
