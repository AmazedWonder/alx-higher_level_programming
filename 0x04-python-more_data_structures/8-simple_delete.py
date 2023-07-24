#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    #  Pop() method removes the key-value pair of key from
    #  dictionary, and returns the value of the removed item
    #  Pass None as the default value,if key is not
    #  in the dictionary, pop() will return None
    my_dict.pop(key, None)

    return my_dict
