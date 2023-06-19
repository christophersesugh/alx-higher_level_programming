#!/usr/bin/python3
"""Rectangle class that inherits the Base class."""


from .base import Base


class Rectangle(Base):
    """Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor function.

        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int): 
            y (int):
            id (str): class id
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            width (int): rectangle width
        """
        self.__width = value

    def width(self):
        """
        width getter
        """
        return (self.__width)

    def height(self, value):
        """
        Set rectangle height.

        Args:
            height (int): rectangle height.
        """
        self.__height = value

    def height(self):
        """
        height getter
        """
        return (self.__height)

    def x(self, value):
        """
        x variable setter
        """
        self.__x = value

    def x(self):
        """x variable getter"""
        return (self.__x)

    def y(self, value):
        """y var setter."""
        self.__y = value

    def y(self):
        """y getter"""
        return (self.__y)
