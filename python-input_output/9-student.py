#!/usr/bin/python3
"""The Student class"""


class Student:
    """The Student Class"""

    def __init__(self, first_name, last_name, age):
        """Create a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Class student to JSON"""
        return self.__dict__
