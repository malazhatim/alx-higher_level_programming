#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "DM": 900,
        "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400
    }
    if not isinstance(roman_string, str):
        return 0
    a = 0
    b = 0
    c = len(roman_string)
    while b < c:
        if b + 1 < l and roman_string[c:c + 2] in roman:
            a += roman[roman_string[c:c + 2]]
            b += 2
        else:
            a += roman[roman_string[b]]
            b += 1
    return a
