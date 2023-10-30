#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """Attributes for Rectangle class
       Args:
       width: width of rectangle
       height: height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize variables"""

        self.width = width
        self.height = height

        @property
        def width(self):
            """
            Find Width
            Return: With of the rectangle
            """

            return self.__width

        @width.setter
        def width(self, value):
            """width setter"""

            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """
            Find Height
            Return: Height of the rectangle
            """

            return self.__height

        @height.setter
        def height(self, value):
            """height setter"""

            if isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
