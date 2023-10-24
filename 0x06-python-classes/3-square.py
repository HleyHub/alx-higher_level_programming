#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """Attributes for Square class
       size(int): size of square
    """

    def __init__(self, size=0):
        """size intitialized if not exception"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Square Area
           Return: area
        """

        area = self.__size ** 2
        return area
