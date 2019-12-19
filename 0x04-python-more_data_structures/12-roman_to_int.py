#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    else:
        number = 0
        prev = 0
        for i in roman_string:
            isNumber = True
            if i == 'I':
                number += 1
            elif i == 'V' and prev == 1:
                number += 5 - 2
                isNumber = False
            elif i == 'X' and prev == 1:
                number += 10 - 2
                isNumber = False
            elif i == 'L' and prev == 1:
                number += 50 - 2
                isNumber = False
            elif i == 'C' and prev == 1:
                number += 100 - 2
                isNumber = False
            elif i == 'D' and prev == 1:
                number += 500 - 2
                isNumber = False
            elif i == 'M' and prev == 1:
                number += 1000 - 2
                isNumber = False
            else:
                if isNumber:
                    if i == 'V':
                        number += 5
                    elif i == 'X':
                        number += 10
                    elif i == 'L':
                        number += 50
                    elif i == 'C':
                        number += 100
                    elif i == 'D':
                        number += 500
                    elif i == 'M':
                        number += 1000
            prev = number
        return number
