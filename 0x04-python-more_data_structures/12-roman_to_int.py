#!/usr/bin/python3
def roman_to_int(roman_string):
    #  Checks if the input roman_string is a string
    if roman_string is None or type(roman_string) != str:
        return 0

    #  Create a dictionary roman_numer that maps each
    #  Roman numeral character to its integer value
    roman_numeral = {"I": 1, "V": 5, "X": 10,
                     "L": 50, "C": 100, "D": 500, "M": 1000}
    output = 0
    prev_val = 0

    #  Loop through each character in roman_string in
    #  reverse order using the [::-1] slice notation
    #  to handle cases like "IV" or "IX" by subtracting the value
    #  of smaller numeral from the value of the larger numeral
    for char in roman_string[::-1]:
        value = roman_numeral[char]

        #  check if the value of the current character is less
        #  than the value of the previous character
        #  If it is,subtract the value of current character
        #  else,adds the value of the current character to output
        if value < prev_val:
            output -= value
        else:
            output += value
        prev_val = value

    return output
