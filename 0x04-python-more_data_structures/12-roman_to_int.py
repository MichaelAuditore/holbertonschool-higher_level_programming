#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    else:
        roman_numbers = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        int_values = [1, 5, 10, 50, 100, 500, 1000]
        newlist = list(roman_string)
        for n in range(0, len(newlist)):
            for r in range(0, len(roman_numbers)):
                if newlist[n] == roman_numbers[r]:
                    newlist[n] = int_values[r]
                    break
        if len(newlist) == 1:
            return newlist[0]
        else:
            add = 0
            for n in range(1, len(newlist)):
                if newlist[n - 1] >= newlist[n]:
                    add += newlist[n - 1]
                else:
                    add -= newlist[n - 1]
            add += newlist[n]
        return add
