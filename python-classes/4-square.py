#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """define a square"""
    def __init__(self, size=0):
        """function that create a square
        Args:
            size (int): size of the square
        Raise:
            TypeError: exception
            ValueError: exception
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate the current square area
        Return:
        int: the current square area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getting the size

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size

        Args:
            value (int): the new size

        Raises:
            TypeError: exception
            ValueError: exception
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
