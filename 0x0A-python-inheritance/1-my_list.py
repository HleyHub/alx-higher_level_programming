#!/usr/bin/python3
"""
Define Class
"""

class MyList(list):
    """
    A class that inherits from a list
    """

    def print_sorted(self):
        """
        Print a sorted list
        """

        print(sorted(self))
