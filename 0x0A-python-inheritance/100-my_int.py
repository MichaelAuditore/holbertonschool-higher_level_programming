#!/usr/bin/python3
class MyInt(int):
    """
    This class evaluates a instance and compare in inverted order
    For example is if equal do the inverted function
    """
    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
