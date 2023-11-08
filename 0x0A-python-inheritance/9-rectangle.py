#!/usr/bin/python3
"""
    Rectangle module
"""


class BaseGeometry:
    """
        BaseGeometry Class
    """

    def area(self):
        """
            public instance method
            Raise:
                Exception: Area not imiplemented

        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Public instance method that validates value
            Args:
                name (string): name
                value(int): Value
            Raise:
                TypeError: When Value is not int
                ValueError: When Value less or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        A class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
            Initializing the class Rectangle
        """

        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """
            Area of the rectangle
        """

        return (self.__height * self.__width)

    def __str__(self):
        """
            Rectangle description in string format
        """

        return("[Rectangle] {}/{}".format(self.__width, self.__height))
