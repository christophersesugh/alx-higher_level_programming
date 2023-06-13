#!/usr/bin/python3
"""Inherits Geometry class."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits BaseGeometry class"""
    def __init__(self, width, height):
        """
        Contructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
