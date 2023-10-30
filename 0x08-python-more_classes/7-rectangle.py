#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """
    class Rectangle
    Private instance attribute:
    (int)width:
    (int)height:
    Public instance attribute:
    number_of_instances:
    print_symbol:
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize variables
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Return: Rectangle made with #"""

        if self.__width == 0 or self.__height == 0:
            return ""
        symb = str(self.print_symbol)
        return ((symb*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """Return: String representation of the rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Return: Delete the instance of rectangle"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
