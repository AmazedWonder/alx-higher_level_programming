#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Map function is used to apply the lambda-
    # function to each element of the input list
    # Lambda returns True or False, if element is divisible by 2 or not
    new_list = list(map(lambda x: x % 2 == 0, my_list))
    # Return the new list
    return new_list
