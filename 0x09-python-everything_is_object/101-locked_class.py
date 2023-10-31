#!/usr/bin/python3

"""Locked class module"""


class LockedClass:
    """
        This class has no class or object attribute. It
        prevents the user from dynamically creating new instance attributes
    """

    __slots__ = "first_name"
