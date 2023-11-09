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

    def to_json(self):
        """
            Retrieves a dictionary representation
            of a Student instance
        """

        return self.__dict__
