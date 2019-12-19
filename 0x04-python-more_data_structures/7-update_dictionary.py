#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return a_dictionary
    else:
        for i in a_dictionary:
            if key not in a_dictionary.keys():
                a_dictionary[key] = value
                return a_dictionary
            if i == key:
                a_dictionary[i] = value
        return a_dictionary
