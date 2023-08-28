#!/usr/bin/python3
"""Defines a JSON file-writing function.

Includes the json module and defines a function called
save_to_json_file. This function takes an object, my_obj, and
a filename as input, and writes the JSON representation of
the object to a text file.

Inside the function, the open function is used to open the file
specified by the filename parameter in write mode ("w").
The json.dump() function is then used to write the JSON
representation of my_obj to the file.

"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
