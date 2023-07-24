#!/usr/bin/python3
def weight_average(my_list=[]):
    #  checks if the input list my_list is empty
    if not my_list:
        return 0
    #  keep track of all the scores
    total_weight = 0
    _sum = 0
    #  loops through each tuple in my_list, and updates
    for tupl_score, tupl_weight in my_list:
        total_weight += tupl_weight
        _sum += tupl_score * tupl_weight
    # calculates the weighted average by dividing
    return _sum / total_weight
