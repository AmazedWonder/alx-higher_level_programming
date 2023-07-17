#!/usr/bin/python3
def max_integer(my_list=[]):
    # If the list is empty
    if len(my_list) == 0:
        return None
    # In descending order
    sort_list = sorted(my_list, reverse=True)
    # Return first elem of sorted list
    return sort_list[0]
