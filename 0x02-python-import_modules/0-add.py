#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add   # import the add function from add_0.py

    a = 1  # Define variables a and b
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
