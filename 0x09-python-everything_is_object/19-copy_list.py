#!/usr/bin/python3
"""Define a class copy_list that returns a copy of a list

the function uses the copy() method of the list object a
to create a copy of the list.

"""


def copy_list(the_list):
    """
    Returns a copy of the input list.

    Args:
        the_list (list): The input list to be copied.

    Returns:
        list: A new list containing the same elements as the input list.
    """
    return the_list.copy()
