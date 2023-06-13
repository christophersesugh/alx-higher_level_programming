#!/usr/bin/python3
"""An empty class."""


class BaseGeometry:
    """A BaseGeometry class."""
    def area(self):
        """
        Raise an area exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer

        Args:
            name (string): inter name
            value (int): integer to be validated
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s}  must be greater than 0".format(name))
