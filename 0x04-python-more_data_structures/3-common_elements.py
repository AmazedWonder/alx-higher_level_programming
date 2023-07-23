#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Use map() and lambda to create a new set with common elements
    alike_set = set(map(lambda x: x if x in set_2 else None, set_1))

    # Remove None values from the set
    alike_set.discard(None)

    # Return the common set
    return alike_set
