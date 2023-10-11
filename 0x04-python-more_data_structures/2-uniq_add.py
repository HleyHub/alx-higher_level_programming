#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = list(dict.fromkeys(my_list))
    return sum(unique_int)
