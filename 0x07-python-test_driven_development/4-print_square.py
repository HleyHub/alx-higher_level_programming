#!/usr/bin/python3

"""
Module that prints prints a square
"""

def print_square(size):
    """
    Return: A square with the character #
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
         print("#" * size)
