#!/usr/bin/python3
"""Project base class."""


class Base:
    """Project base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor function.

        Args:
            id (string): use to identify class id's and avoid duplication.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
