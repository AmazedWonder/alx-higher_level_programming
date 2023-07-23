#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a new list of unique values using filter() and lambda
    unique_val = list(filter(lambda x: my_list.count(x) == 1, my_list))

    # Use map() to convert the unique values to integers
    unique_int_val = list(map(int, unique_val))

    # Add up the unique values, use the built-in sum() function
    unique_add = sum(unique_int_val)

    # Return the sum of unique values
    return unique_add
