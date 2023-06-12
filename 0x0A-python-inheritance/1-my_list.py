#!/usr/bin/python3
"""Inherits a super class."""


class MyList(list):
    """Inherit a list super class."""
    def print_sorted(self):
        """
        print list in sorted order.

        Return:
            sorted list
        """
        print(sorted(self))
