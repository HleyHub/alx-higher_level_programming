#!/usr/bin/python3
"""
    Pascal triangle module
"""


def pascal_triangle(n):
    """
        Return: a list of lists of integers
        representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []
    ans = []
    my_list = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(my_list[j] + my_list[j - 1])
        my_list = row
        ans.append(row)
    return ans
