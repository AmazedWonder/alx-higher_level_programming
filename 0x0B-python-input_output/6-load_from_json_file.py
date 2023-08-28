#!/usr/bin/python3
"""Defines a JSON file-reading function.

Includes the json module and defines a function called
load_from_json_file. This function takes a filename as
input and reads the contents of the JSON file, then returns
the corresponding Python object representation.

Inside the function, the open function is used to open the
file specified by the filename parameter. The default mode
for open is read mode ("r"). The json.load() function is then used
to parse the contents of the file and convert it into a Python object.

"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
