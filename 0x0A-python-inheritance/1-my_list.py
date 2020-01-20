#!/usr/bin/python3
class MyList(list):
    """Class list inherits list"""
    def print_sorted(self):
        new = MyList()
        new = self.copy()
        new.sort()
        print(new)
