#!/usr/bin/python3

"""
Module that prints a square
"""

def print_square(size):
    """
        Return: Square with the character #
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
         print("#" * size)
