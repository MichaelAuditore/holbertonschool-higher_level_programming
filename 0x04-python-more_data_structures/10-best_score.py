#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        name = ""
        for i in a_dictionary:
            best = 0
            if (a_dictionary[i] > best):
                name = i
        return name
