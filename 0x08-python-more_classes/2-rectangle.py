#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """
    class Rectangle
    Private instance attribute:
    (int)width:
    (int)height:
    """

    def __init__(self, width=0, height=0):
        """
        Initialize variables
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Find width
        returns: width of the Rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
        value: the value to be set
        raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Find height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
        value: the value to be set
        raises:
        TypeError: height must be an integer
        ValueError: height must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return: Area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Return: Rectangle of the perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
