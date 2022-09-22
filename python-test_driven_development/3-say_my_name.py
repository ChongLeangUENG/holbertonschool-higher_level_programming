#!/usr/bin/python3
"""
Function that says my name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that print the full name

    Args:
        first_name: string of first name
        last_name: string of last name
    """

    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
