#!/usr/bin/python3
"""Defines a Rectangle class.

In this updated version of previous 2-rectangle.py, the __str__
method is overridden to provide a string representation of the
rectangle using the "#" character. If the width or height is
equal to 0, an empty string is returned.

The __repr__ method is also overridden to provide a string
representation that can be used to recreate the object.

"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):

        """Initialize a new Rectangle.

        Args:
            width (int, optional): The width of the new rectangle.
            Defaults set to 0
            height (int, optional): The height of the new rectangle.
            Defaults set to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle for users to change it
        value but restricted using Raises, to get the type and value
        that the user is expected to input..

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_str = []
        for i in range(self.__height):
            [rect_str.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect_str.append("\n")
        return ("".join(rect_str))

    #def __repr__(self):
        """
        Return a string representation that can be used to recreate the object.

        Returns:
            str: A string representation of the rectangle object.
        """
        #return f"Rectangle({self.width}, {self.height})"
