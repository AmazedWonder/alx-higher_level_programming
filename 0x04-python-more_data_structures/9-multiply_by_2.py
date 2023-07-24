#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    #  Create a new dictionary new_dict
    new_dict = {}

    #  Use for loop with the items() to loop through
    #  both keys and values at the same time
    for key, val in a_dictionary.items():

        #  Assigns the result of val * 2 to
        #  the corresponding key in new_dict
        new_dict[key] = val * 2

    return new_dict
