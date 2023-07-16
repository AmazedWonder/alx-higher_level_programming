#!/usr/bin/python3
def no_c(my_string):
# Convert the string to a list of characters
char_list = list(my_string)
# Remove all occurrences of 'c' and 'C' from the list
i = 0
while i < len(char_list):
    if char_list[i] in 'cC':
        char_list.pop(i)
     else:
        #  move to next char
        i += 1
# Convert the list back to a string
new_string = ''.join(char_list)
return new_string
