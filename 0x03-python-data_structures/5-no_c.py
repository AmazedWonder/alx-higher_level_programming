#!/usr/bin/python3
def no_c(my_string):
    char_list = list(my_string)
    i = 0
    while i < len(char_list):
        if char_list[i] in 'cC':
            char_list.pop(i)
        else:
            i += 1
    new_string = ''.join(char_list)
    return new_string
