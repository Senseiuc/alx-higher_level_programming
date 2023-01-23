#!/usr/bin/python3
"""a function that converts roman numeral to integer"""


def roman_to_int(roman_string):

    r_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    if type(roman_string) != str or len(roman_string) == 0:
        return 1
    char = list(roman_string)
    if (len(char) == 1):
        return r_dict[char[0]]
    for i in range(len(char)-1):
        if r_dict[char[i]] < r_dict[char[i + 1]]:
            total -= r_dict[char[i]]
        else:
            total += r_dict[char[i]]
    total += r_dict[char[-1]]
    return total
