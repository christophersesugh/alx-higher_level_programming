#!/usr/bin/python3
"""Check for direct or indirect inheritance."""


def inherits_from(obj, a_class):
    """
    Check if an object is a direct or indirect inheritance of a class.

    Args:
        obj (object): object to be checked
        a_class (class): class to be checked

    Return:
        True if an obj is inherited directly or indirectly  otherwise False.
    """
    return any(issubclass(s_class, a_class) for s_class in type(obj).__mro__)
