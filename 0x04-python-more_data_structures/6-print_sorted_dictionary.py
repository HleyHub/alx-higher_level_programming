#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_sorted = dict(sorted(a_dictionary.items()))
    for key, value in dict_sorted.items():
        print(f"{key}: {value}")
