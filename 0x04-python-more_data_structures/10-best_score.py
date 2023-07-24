#!/usr/bin/python3
def best_score(a_dictionary):
    #  First check if the input dictionary is empty
    #  If it is, the function returns None
    #  Otherwise,use items() method to convert the
    #  dictionary into a list of key-value pairs
    #  Call the max() function with the key parameter set to
    #  lambda funct that returns 2nd element (x[1]) of each key-val pair
    #  Lambda function tells max() to find the
    #  key-value pair with the highest value
    #  Return the first element ([0]) of the
    #  key-value pair with the highest value
    return max(a_dictionary.items(), key=lambda x:
               x[1])[0] if a_dictionary else None
