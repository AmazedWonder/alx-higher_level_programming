#!/usr/bin/python3
# Make the file usable as a script as well as an importable module
if __name__ == "__main__":
    import sys
    # Exclude the first argument, which is the script name
    arg = sys.argv
    len_args = len(arg) - 1
    # Print the number of arguments and the list of arguments
    if len_args > 1:
        print("{} arguments:".format(len_args))
        for i in range(1, len_args + 1):
            print("{}: {}".format(i, arg[i]))

    elif len_args == 0:
        print("{} arguments.".format(len_args))

    else:
        print("{} argument:".format(len_args))
        print("{}: {}".format(len_args, arg[1]))
