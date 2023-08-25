#!/usr/bin/python3
"""Defines an inherited list class MyList.

defines a class MyList that inherits from the built-in
list class. It adds a new method print_sorted to the MyList
class, which prints the list in sorted ascending order.

The print_sorted method uses the sorted() function to sort the
elements of the list (self) in ascending order. The sorted list
is then printed using the print() function.

"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
