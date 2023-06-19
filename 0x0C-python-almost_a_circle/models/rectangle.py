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
            x (int): x dimension
            y (int): y dimensio
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def x(self):
        """x variable getter"""
        return (self.__x)

    def y(self, value):
        """y var setter."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def y(self):
        """y getter"""
        return (self.__y)

    def area(self):
        """Area getter"""
        return (self.__width * self.__height)

    def display(self):
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
            self.__x, self.__y, self.__width, self.__height))
