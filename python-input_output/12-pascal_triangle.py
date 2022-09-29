#!/usr/bin/python3
"""Function that return a list of lists of integers"""


def pascal_triangle(n):
    """Create a function that returns a list of lists of integers
    representing the Pascal triangle of n"""
    if n <= 0:
        return []
