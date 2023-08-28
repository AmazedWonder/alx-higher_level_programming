#!/usr/bin/python3
"""Defines a class Student.

This updated code includes a new method called reload_from_json
in the Student class. The reload_from_json method allows you to
replace all attributes of a Student object with the key-value
pairs from a given dictionary (json).

Student object named student is created with the first name "John",
last name "Doe", and age 20. The reload_from_json method is called
on the student object with a dictionary json_data containing new
attribute values. The reload_from_json method replaces all attributes
of the student object with the values from the json_data dictionary.
The updated attribute values are printed before and after the method call.

The reload_from_json method utilizes the setattr function to set the
attribute values of the Student object dynamically based on the
key-value pairs in the json dictionary.

This method allows update of the attributes of a Student object
using data from a dictionary, providing a convenient way to reload or
update object attributes from an external source.

"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {key: getattr(self, key)
                    for k in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key(name)/value pairs to replace attributes with.
        """
        for key, val in json.items():
            setattr(self, key, val)
