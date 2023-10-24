#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elt = 0
    try:
        for j in range(0, x):
            print(my_list[j], end="")
            elt = elt + 1
    except IndexError:
        pass
    print()
    return elt
