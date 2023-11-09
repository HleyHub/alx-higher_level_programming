#!/usr/bin/python3
"""
    Class Student module
"""


class Student():
    """
        A class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialization of class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieves a dictionary representation of a Student instance
        """

        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
