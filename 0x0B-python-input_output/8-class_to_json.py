#!/usr/bin/python3
"""
    Dictionary description with simple data structure
    JSON serialization of an object
"""


def class_to_json(obj):
    """
        Return: Dictionary description with simple data structure
        JSON serialization of an object
    """

    return obj.__dict__
