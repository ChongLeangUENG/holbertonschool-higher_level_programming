#!/usr/bin/python3
"""function that reads a text file and print it"""


def read_file(filename=""):
    """function that reads a text file and print it"""
    with open(filename) as file:
        print(file.read(), end='')
