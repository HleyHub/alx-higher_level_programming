#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100,
            'D': 500, 'M': 1000}
    total = 0
    old_value = 0
    for numeral in reversed(roman_string):
        value = roman_numerals.get(numeral, 0)
        if value < old_value:
            total = total - value
        else:
            total = total + value
        old_value = value
    return total
