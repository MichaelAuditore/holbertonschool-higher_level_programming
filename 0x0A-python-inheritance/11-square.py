#!/usr/bin/python3
class BaseGeometry:
    """
    Class to define if the object have Base Geometry
    """
    def area(self):
        """
        define the area for a geometry object
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        define a validator for a value will be used into the function
        """
        if (type(value) is not int):
            raise TypeError(name + ' must be an integer')
        if (value <= 0):
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """
    Class to define a rectangle as BaseGeometry
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        s = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return s


class Square(Rectangle):
    """
    Class to define a square from Rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        s = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return s
