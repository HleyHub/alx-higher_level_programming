#!/usr/bin/python3
"""
Define Class
"""


class MyList(list):
    """
    subclass:
    class MyList
    """

    def print_sorted(self):
        """
        Print a sorted list
        """

        print(sorted(self))
