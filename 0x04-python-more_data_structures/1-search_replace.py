#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None or search is None or replace is None:
        return my_list
    new = []
    idx = 0
    for i in my_list:
        new.append(i)
    for h in new:
        if h == search:
            new[idx] = replace
        idx += 1
    return new
