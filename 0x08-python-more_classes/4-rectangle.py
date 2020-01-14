#!/usr/bin/python3


class Rectangle:
    """
    Class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        _str = ""
        if self.__width == 0 or self.__height == 0:
            return _str
        a, b = self.__width, self.__height
        for i in range(b):
            for j in range(a):
                _str += "#"
            _str += "\n"
        return _str[:-1]

    def __repr__(self):
        return ("Rectangle(" + str(self.__width) + ","
                + str(self.__height) + ")")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
