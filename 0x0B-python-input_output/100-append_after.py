#!/usr/bin/python3
"""
    Append after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
        A function that inserts a line of text to a file
        after each line containing a specific string
    """

    with open(filename, "r+", encoding="utf-8") as myFile:
        stg = ""
        for line in myFile:
            stg += line
            if search_string in line:
                stg += new_string
        myFile.seek(0)
        myFile.write(stg)
