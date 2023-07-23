#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a new set to store unique values
    unique_set = set(my_list)

    # Add up the unique values, use the built-in sum() function
    unique_add = sum(unique_set)

    # Return the sum of unique values
    return unique_add
