#!/usr/bin/python3
"""Define a Rectangle class that defines a rectangle"""


class Rectangle:
    """Defines a rectangle."""
    def __init__(self, width=0, height=0):
        """
        Construct the Rectangle class

        Args:
            width (int): rectangle width.
            height (int): rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Return rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): the height of the rectangle to be set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Return rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): the width of the rectangle to be set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def area(self):
        """Return the area of a rectangle."""
        a = self.__width * self.__height
        return a

    @property
    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
