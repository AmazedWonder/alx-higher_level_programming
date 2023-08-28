#!/usr/bin/python3
"""Defines a file-appending function.

Defines a function called append_write that appends
a string to the end of a UTF-8 encoded text file.

The function takes two parameters: filename and text. filename
specifies the name of the file to which the string will be appended,
and text is the string that will be appended to the file.

Inside the function, the file is opened using the open function with
the filename and the mode parameter set to "a" to indicate that the
file should be opened in append mode. This means that new content will
be added to the end of the file, rather than overwriting the existing
content. The encoding parameter is set to "utf-8" to ensure that the
text is encoded in UTF-8.

The file is opened in a with statement, which ensures that the file
is properly closed after appending, even if an exception occurs.

The write method of the file object f is used to append the text
to the file. The method returns the number of characters appended.

The function returns the value returned by the write method, which
represents the number of characters appended to the file.

"""


def append_write(filename="", text=""):
    """Appends a string to the end of UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
