#!/usr/bin/python3
"""Function that write a string to a text file"""


def write_file(filename="", text=""):
    """Write a string to text file and print number of char"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
