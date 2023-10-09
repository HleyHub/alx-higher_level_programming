#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_entier = my_list[0]
    for j in my_list:
        if (j > max_entier):
            max_entier = j
    return (max_entier)
