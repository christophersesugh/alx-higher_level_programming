#!/usr/bin/python3
"""A function that compares two objects"""


def is_same_class(obj, a_class):
    """
    Compares if the instance of the first object is of the second object.

    Args:
        obj (object): first object
        a_class (object): second object

    Return:
        True is they of the same instances otherwise False
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
