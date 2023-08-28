#!/usr/bin/python3
"""Defines a class Student.

This updated code adds an additional functionality to the
to_json method of the Student class. The to_json method now
accepts an optional attrs parameter, which is a list of attribute
names. If the attrs parameter is provided and contains valid
string elements, the method returns a dictionary representation
of the Student object containing only the specified attributes.

Student object named student is created with the first name "John",
last name "Doe", and age 20. The to_json method is called on the
student object without passing any attributes, resulting in a
dictionary representation of all the student's attributes.
The resulting dictionary is stored in the json_dict_all
variable and printed to the console.

The to_json method also demonstrates the ability to select specific
attributes by passing a list of attribute names. In the second call
to to_json, the attributes first_name and age are specified. As a
result, only those attributes are included in the dictionary
representation, which is stored in the json_dict_selected
variable and printed to the console.

If the attrs parameter is not provided or is not a list of strings,
the method falls back to returning the dictionary representation
of all the attributes using self.__dict__.

This updated code provides flexibility in selecting specific attributes
to include in the JSON representation of a Student object.

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
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
