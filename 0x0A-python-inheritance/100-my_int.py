#!/usr/bin/python3
"""
    class MyInt module
"""


class MyInt(int):
    """
        Class MyInt that inherits from int
    """
    def __eq__(self, x):
        """
        Initialization of eq
        """

        return not super().__eq__(x)

    def __ne__(self, x):
        """
        Initialization for greater than
        """

        return not super().__ne__(x)
