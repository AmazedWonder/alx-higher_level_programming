#!/usr/bin/python3
# make the file usable as a script as well as an importable module
if __name__ == "__main__":
    # import the add function from add_0.py
    from add_0 import add

    # Define variables a and b
    a = 1
    b = 2

    # Call add function with arguments a and b
    # and print the result using string formatting
    print("{} + {} = {}".format(a, b, add(a, b)))
