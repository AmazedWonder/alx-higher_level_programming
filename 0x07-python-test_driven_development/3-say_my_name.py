#!/usr/bin/python3
"""Defines a name printing function.

This function, first checks if both first_name and last_name
are strings using the isinstance() function. If either of them
is not a string, we raise a TypeError with the appropriate message.

Then, use an if-else statement to determine whether to print full
name or just the first name based on whether last_name is provided.
The print() function is used to display the formatted name string.

The last_name parameter is optional and has a default value of an
empty string. This means that if last_name is not provided when
calling the function, it will default to an empty string.

"""


def say_my_name(first_name, last_name=""):
    """
    Prints name in the format "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith

        >>> say_my_name("Bob")
        My name is Bob
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
