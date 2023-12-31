#!/usr/bin/python3
"""
    A function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """
        adds a new attribute
        raise:
            TypeError: can't add new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
