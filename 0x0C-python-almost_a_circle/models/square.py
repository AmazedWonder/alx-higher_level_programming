#!/usr/bin/python3
"""Defines a class named "Square" that represents a square.
The class inherits from the "Rectangle" class, which means
it inherits the attributes and methods of the Rectangle
class and adds its own specific functionality for squares

The constructor (__init__) initializes a new Square object with
the provided size, x-coordinate, y-coordinate, and id. It
calls the parent class's constructor (super()
This ensures that the Square is initialized as a special case
of a Rectangle with equal width and height.

The size property provides a getter and setter for the size
attribute of the square. It maps the size attribute to
the width attribute of the underlying Rectangle.

The update method allows updating the attributes of the
square using either positional arguments or keyword arguments.
It checks if positional arguments (args) or keyword arguments (kwargs)
are provided and updates the corresponding attributes accordingly.

The to_dictionary method returns a dictionary representation of
the square, containing its attributes (id, size, x, and y).It leverages
the parent class's width attribute to represent the size.

The __str__ method provides a string representation of the square
that can be used with the print function or str function. It
displays the square's id, x and y coordinates, and size
(which is mapped to the width attribute).

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
