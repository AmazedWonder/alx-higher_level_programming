#!/usr/bin/python3
"""Defines a class Student.

Defines a Student class with an __init__ method and a to_json
method. The __init__ method is used to initialize a new Student
object with the provided first name, last name, and age. The
to_json method returns a dictionary representation of the Student
object using the __dict__ attribute.

Student object named student is created with the first name "John",
last name "Doe", and age 20. The to_json method is called on the
student object, which returns a dictionary representation of the
student's attributes. The resulting dictionary is stored in the
json_dict variable and printed to the console.

The to_json method utilizes the __dict__ attribute of the object,
which contains the attribute-value pairs of the object. By returning
self.__dict__, the method provides a dictionary representation of the object.

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

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
