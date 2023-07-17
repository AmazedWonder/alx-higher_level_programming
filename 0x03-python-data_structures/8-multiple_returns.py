#!/usr/bin/python3
def multiple_returns(sentence):
    # Get length of sentence
    length = len(sentence)
    # Get 1st character in the sentence or None if empty
    first_char = sentence[0] if length > 0 else None
    # Return a tuple with length and first char
    mul_ret = length, first_char
    return (mul_ret)
