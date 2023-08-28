#!/usr/bin/python3
"""Defines a text file insertion function.

Defines a function append_after that inserts text after each
line containing a given string in a file. The function takes
three arguments: filename (the name of the file), search_string
(the string to search for within the file), and new_string
(the string to insert).

The function reads the contents of the file, line by line, and
appends each line to a text variable. If the search_string is found
in a line, it also appends the new_string after that line. Finally,
the updated text is written back to the file, overwriting its
previous contents.

This code will open the file named "file.txt" and search for lines
containing the string "search". It will insert the string
"inserted text" after each matching line in the file.

While the function achieves the desired functionality, it can
be improved in terms of efficiency. Currently, it reads the
entire file into memory and writes it back after making modifications.
This approach can be inefficient for large files.

A more efficient approach is to read the file line by line and write
to a temporary file, only appending the new_string when necessary.
Once the processing is complete, the temporary file can be renamed
to replace the original file.

This updated code uses a temporary file (temp_filename) to write
the modified contents. It opens the input file (filename) for
reading and the temporary file for writing. It then iterates
over each line in the input file, writing the line to the temporary
file and appending the new_string if the search_string is found.

Finally, it uses os.replace to replace the original file with the
temporary file, effectively updating the file with the modified contents.

This approach avoids reading the entire file into memory and provides
better efficiency, especially for large files.

"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
