#!/usr/bin/python3
"""Geometry module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle that in herits from basegeometry"""
    def __init__(self, width, height):
        """Create a rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculator the area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Method print string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
