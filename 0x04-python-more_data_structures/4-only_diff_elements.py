#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # The ^ operator is used to find the symmetric diff of the sets
    # The symmetric difference contains elements that \
    # are in either of the input sets, but not in both
    # The result is a new set that contains
    # elements that are unique to each set
    odd_set = set_1 ^ set_2

    # Return the unique set
    return odd_set
