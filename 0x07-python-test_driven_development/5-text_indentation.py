#!/usr/bin/python3

"""
Text indentation module
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = True
    for c in text:
        if flag and c.isspace():
            continue
        print(c, end='')
        if c in ['.', '?', ':']:
            print("\n")
            flag = True
        else:
            flag = False
