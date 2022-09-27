#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry():
    """Empty class BaseGeometry"""
    def area(self):
        """raises an Exception with the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value
        Args:
            name: a string
            value: Value of geometry
        """
        if isinstance(value, int) is False:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
