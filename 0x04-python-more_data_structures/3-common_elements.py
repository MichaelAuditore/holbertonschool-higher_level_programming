#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return set_1
    new = []
    for i in set_1:
        for h in set_2:
            if i == h:
                new.append(i)
    return new
