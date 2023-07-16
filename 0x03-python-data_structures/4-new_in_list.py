#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    # Create a new list with the same elements as my_list
    temp = my_list[:]
    # Replace the element at position idx with the new element
    temp[idx] = element
    return temp
