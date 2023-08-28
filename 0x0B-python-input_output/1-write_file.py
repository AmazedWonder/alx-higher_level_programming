#!/usr/bin/python3
"""Defines a file-writing function.

Defines a function called write_file that writes
a string to a UTF-8 encoded text file.

The function takes two parameters: filename and text. filename
specifies the name of the file to be written, and text is the
string that will be written to the file.

Inside the function, the file is opened using the open function
with the filename and the mode parameter set to "w" to indicate that
the file should be opened for writing. The encoding parameter is
set to "utf-8" to ensure that the text is encoded in UTF-8.

The file is opened in a with statement, which ensures that the
file is properly closed after writing, even if an exception occurs.

The write method of the file object f is used to write the text to
the file. The method returns the number of characters written.

The function returns the value returned by the write method, which
represents the number of characters written to the file.

"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
