#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    #  creates a copy of input dictionary using copy() method
    tmp_dict = a_dictionary.copy()

    #  loops over the keys of the tmp_dict using the keys()
    for k in tmp_dict.keys():
        #  checks if value is equal to the input value value
        if tmp_dict[k] == value:
            #  If it is,use pop() method to remove the
            #  key-value pair from original dictionary
            a_dictionary.pop(k)

    #  Return modified dictionary
    return a_dictionary
