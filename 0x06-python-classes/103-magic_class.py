#!/usr/bin/python3
import math


class MagicClass:

    """ This Class stores the data of a circle
    to get the area and circunference"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    """ function to get the area """
    def area(self):
        return ((self.__radius ** 2) math.pi)
    """ function to get the circumference of the radius of circle"""
    def circumference(self):
        return (2 * math.pi * self.__radius)
