#!/usr/bin/python3
"""Defines a function that adds attributes to objects.

allows adding a new attribute to an object if possible.

How the function works:

obj is the object to which the attribute will be added.
att is a string representing the name of the attribute.
value is the value that will be assigned to the attribute.

The function first checks if the obj has a __dict__ attribute.
The __dict__ attribute is a dictionary that stores the object's
attributes and their corresponding values. It is present in most
objects that allow dynamically adding new attributes.

If obj does not have a __dict__ attribute, it means that the object
does not support adding new attributes, and a TypeError is raised
with the message "can't add new attribute."

If obj has a __dict__ attribute, the setattr function is used to add
the new attribute to the object. The setattr function takes three
arguments: the object (obj), the attribute name (att), and the value
to be assigned (value). This effectively adds the attribute to the
object with the specified value.

"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
