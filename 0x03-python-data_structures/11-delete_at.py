#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # If the index is negative or out of range, return same list
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Create a new list that contains all
    # elements except elem at the given index
    del (my_list[idx])
    #  Return mofdified list
    return my_list
