#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elt = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j], end=""))
            elt = elt + 1
        except (TypeError, ValueError):
            pass
    print()
    return elt
