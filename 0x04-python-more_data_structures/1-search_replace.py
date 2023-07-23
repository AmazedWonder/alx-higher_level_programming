#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Use map and lambda to replace the
    # Search value with the replace value
    new_list = list(map(lambda x: replace if x == search else x, my_list))

    # Return the new list
    return new_list
