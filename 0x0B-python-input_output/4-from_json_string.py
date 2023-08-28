#!/usr/bin/python3
# 4-from_json_string.py
"""Defines a JSON-to-object function.

Includes the json module and defines a function called
from_json_string. This function takes a JSON-formatted
string, my_str, as input and returns the corresponding
Python object representation.

Inside the function, the json.loads() function is used to
parse the my_str JSON string and convert it into a Python object.
The loads() function deserializes the JSON string into a Python object.

"""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
