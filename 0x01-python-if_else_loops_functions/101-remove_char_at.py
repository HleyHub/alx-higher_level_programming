#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    if n > len(str) or n < 0:
        return str
    for j in str:
        if j != str[n]:
            strcpy += j
    return strcpy
