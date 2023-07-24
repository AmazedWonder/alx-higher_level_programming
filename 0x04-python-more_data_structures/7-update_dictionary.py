#!/usr/bin/python3
#  dictionary a_dictionary, a key key, and a value value as input
def update_dictionary(a_dictionary, key, value):

    #  update dict by setting the value of the key to value
    #  If the key already exists in dictionary,
    #  its value will be replaced with value
    #  if not,a new key/value pair will be created
    a_dictionary[key] = value

    return a_dictionary
