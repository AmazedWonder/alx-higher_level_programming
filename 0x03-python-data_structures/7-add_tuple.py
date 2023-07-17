#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples with zeros if they are smaller than 2 elements
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    # if bigger than 2 take only the first 2 elements of the tuples
    a, b = tuple_a[:2]
    c, d = tuple_b[:2]
    # Add the corresponding elements and return the result as a tuple
    return (a + c, b + d)
