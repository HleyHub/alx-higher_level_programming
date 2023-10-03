#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    if last_digit <0:
        print("{}".format(-last_digit), end='')
        return -last_digit
    else:
        print("{}".format(last_digit), end='')
        return last_digit
