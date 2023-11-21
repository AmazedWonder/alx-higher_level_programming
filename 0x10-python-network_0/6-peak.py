#!/usr/bin/python3
"""
Module Docs
"""


def _fp_recurs(list_of_integers, begin, end):
    """
    Recursive helper function to perform binary
    search for peak element within a given range.
    """
    # Base case: if the range has less than 2 elements, return None
    if end - begin < 2:
        return None

    mid = (begin + end) // 2

    # Check if the middle element is a peak by comparing it with its neighbors
    if (list_of_integers[mid] >= list_of_integers[mid - 1]
            and list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]

    # Recurse on the left and right halves of the range
    return (_fp_recurs(list_of_integers, begin, mid)
            or _fp_recurs(list_of_integers, mid, end))


def find_peak(list_of_integers):
    """
    Function to find a peak element in the given list of integers.
    """
    # Check if the list has more than one element
    if len(list_of_integers) > 1:
        # Check if the first element is a peak
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        # Check if the last element is a peak
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]

        # Call the recursive helper function to find the
        # peak within the range [0, len(list_of_integers))
        return _fp_recurs(list_of_integers, 0, len(list_of_integers))

    # Handle the case when the list is empty
    if not list_of_integers:
        return None

    # Handle the case when the list has only one element
    return list_of_integers[0]
