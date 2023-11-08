#!/usr/bin/python3
"""
    Square class Module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Class Square
    """

    def __init__(self, size):
        """
            Initializing the square base
        """

        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
            Area of the square
        """

        return self.__size ** 2

    def __str__(self):
        """
            __str__
        """

        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
