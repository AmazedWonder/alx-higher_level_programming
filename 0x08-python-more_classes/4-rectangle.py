#!/usr/bin/python3
"""Defines a Rectangle class.

The __init__ method is the constructor of the class. It
initializes a new instance of the Rectangle class with
the given width and height.

The width and height properties are implemented using the
@property decorator. They allow getting and setting the width
and height of the rectangle while performing validation checks.
If the values provided are not integers or if they are less than
zero, the corresponding setter methods raise TypeError or
/ValueError exceptions, respectively.

The area method calculates and returns the area of the rectangle
by multiplying its width and height.

The perimeter method calculates and returns the perimeter of the
rectangle. If either the width or height is zero, the perimeter
is considered zero.

The __str__ method returns the printable representation of the rectangle.
It represents the rectangle with the '#' character. If either the width
or height is zero, it returns an empty string.

The __repr__ method returns the string representation of the rectangle.
It returns a string that can be used to recreate the rectangle object.

"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_str = []
        for i in range(self.__height):
            [rect_str.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect_str.append("\n")
        return ("".join(rect_str))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect_str = "Rectangle(" + str(self.__width)
        rect_str += ", " + str(self.__height) + ")"
        return (rect_str)
