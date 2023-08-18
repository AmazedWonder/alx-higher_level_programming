#!/usr/bin/python3
"""Defines a Rectangle class.

A new class attribute number_of_instances has been added to the
Rectangle class. This attribute keeps track of the number of
Rectangle instances that have been created.

The number_of_instances attribute is defined outside of
any methods and is set to 0 initially.

In the __init__ method, the number_of_instances attribute is incremented
by 1 using type(self).number_of_instances += 1. This line ensures that 
every time a new Rectangle instance is created, the number_of_instances
attribute is updated accordingly.

In the __del__ method, the number_of_instances attribute is decremented
by 1 using type(self).number_of_instances -= 1. This line ensures that
when a Rectangle instance is deleted, the number_of_instances attribute
is updated to reflect the change.

"""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
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

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

