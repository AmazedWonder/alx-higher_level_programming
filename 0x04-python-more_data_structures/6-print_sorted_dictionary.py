#!/usr/bin/python3
#  defines a function name and takes my_dict as arg
def print_sorted_dictionary(my_dict):

    #  Using the sorted() function,create a sorted
    #  list of the keys in the dictionary my_dict
    #  Loop through each key in the sorted list
    #  and assign it to the variable k in each iteration
    for key in sorted(my_dict.keys()):

        #  Print each key-value pair in the dict in sorted order
        #  use the format() method to create a string that
        #  combines the key and value of each item in the dictionary
        print("{}: {}".format(key, my_dict[key]))
