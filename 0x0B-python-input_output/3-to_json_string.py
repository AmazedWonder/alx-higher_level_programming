#!/usr/bin/python3
"""Defines a string-to-JSON function.

Includes the json module and defines a function called
to_json_string. This function takes an object, my_obj, as input
and returns the JSON representation of that object as a string.

Inside the function, the json.dumps() function is used to convert
the my_obj object to a JSON-formatted string. The dumps() function
serializes the object into a JSON string representation.

"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
