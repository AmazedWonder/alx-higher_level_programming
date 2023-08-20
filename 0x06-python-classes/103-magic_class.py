#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode 

Defines a class called MagicClass that represents a circle

The MagicClass class has an __init__ method that is called when
a new instance of the class is created. It initializes the magic
class with a given radius. The radius is passed as an argument,
with a default value of 0. The method checks if the provided radius
is a number (either float or int). If it is not, a TypeError is raised.
Otherwise, the radius is assigned to the private attribute __radius.

The class has two methods: area and circumference. The area method
calculates and returns the area of the circle using the formula
radius^2 * pi. It accesses the value of the private attribute __radius.

The circumference method calculates and returns the circumference of
the circle. It uses the formula 2 * pi * radius to calculate the
circumference. It also accesses the value of the private attribute __radius.

"""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)

