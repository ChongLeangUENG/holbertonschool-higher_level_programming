#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False

    Args:
        obj: Object
        a_class: Class type
    """
    return isinstance(obj, a_class)
