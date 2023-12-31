#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
    }
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    total = 0
    idx = 0

    while idx < len(roman_string):
        if idx+1 < len(roman_string) and roman_string[idx:idx+2] in numerals:
            total += numerals[roman_string[idx:idx+2]]
            idx += 2
        else:
            total += numerals[roman_string[idx]]
            idx += 1

    return total
