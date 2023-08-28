#!/usr/bin/python3
"""Defines a text file-reading function.

Defines a function called read_file that reads the contents
of a UTF-8 encoded text file and prints it to the standard
output (stdout).

The function takes an optional parameter filename, which
specifies the name of the file to be read. If no filename
is provided, an empty string is used as the default value.

Inside the function, the file is opened using the open function,
which takes the filename and the encoding parameter set to "utf-8"
to ensure that the file is treated as UTF-8 encoded. The file is
opened in a with statement, which ensures that the file is properly
closed after reading, even if an exception occurs.

The contents of the file are read using the read method of the
file object f, and then printed to the standard output using the
print function. The end="" argument is used to prevent print from
adding an extra newline character after printing the file contents.

"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
