#!/usr/bin/python3
"""Defines a function that prints with '#'.

Checks if the size parameter is an integer or a float.
If it's not, a TypeError is raised with a message..

If the size is a float, it further checks if it's less than 0.
If it is, a TypeError is raised, and if it's greater than or
equal to 0,a TypeError specify that size must be an integer is raised.

If the size is an integer, it checks if it's less than 0, and if
it is, a ValueError is raised with the appropriate message.

if the size is valid, a square is printed using the print() function
and a loop repeats size times, prints '#' size times on each iteration.

"""


def print_square(size):
    """
    Prints a square with the character '#' of the given size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or a float.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####

        >>> print_square(3)
        ###
        ###
        ###

        >>> print_square(0)
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
