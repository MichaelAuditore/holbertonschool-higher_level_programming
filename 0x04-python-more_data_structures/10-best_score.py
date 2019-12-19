#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        best = 0
        for i in a_dictionary:
            if best == 0:
                name = i
                best = a_dictionary[i]
            else:
                if a_dictionary[i] > best:
                    best = a_dictionary[i]
        for h in a_dictionary:
            if best == a_dictionary[h]:
                return h
