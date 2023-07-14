#!/usr/bin/python3
if __name__ == "__main__":
    import sys

args = sys.argv[1:]

# Use a list comprehension to convert args to a list of integers
int_list = [int(arg) for arg in args]

# Sum() function adds up the integers
total = sum(int_list)

print(total)
