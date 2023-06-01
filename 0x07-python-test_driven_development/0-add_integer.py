#!/usr/bin/python3
"""Define a function that add two ints."""


def add_integer(a, b=98):
    """A function that add two integers and return their sum.

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: the sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)
    return (a + b)
