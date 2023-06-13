#!/usr/bin/python3
"""Checks for class and object instances."""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or a super class.

    Args:
        obj (object): the object to be checked
        a_class (class): object to be checked

    Return:
        True if they are of the same instance otherwise False.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
