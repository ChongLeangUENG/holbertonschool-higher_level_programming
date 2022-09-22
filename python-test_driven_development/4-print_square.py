#!/usr/bin/python3
"""
Function that print square
"""


def print_square(size):
    """
    Function that print a square

    Args:
        size (int): size of the square
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
