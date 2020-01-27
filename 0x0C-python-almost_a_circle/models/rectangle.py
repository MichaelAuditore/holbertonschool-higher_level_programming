#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """
    Class to define a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor of the class Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Displays a rectangle using # to draw it"""
        a, b = self.width, self.height
        for y in range(self.y):
            print("")
        for i in range(b):
            for x in range(self.x):
                print(" ", end="")
            for j in range(a):
                print("#", end="")
            print("")

    def __str__(self):
        """Return an string representation of object"""
        s = "[Rectangle] ("
        s += str(self.id) + ") "
        s += str(self.x) + "/" + str(self.y)
        s += " - " + str(self.width) + "/" + str(self.height)
        return (s)

    def update(self, *args, **kwargs):
        """Update attributes for an object"""
        if (len(args) != 0):
            attr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of an object"""
        dic = {"x": self.x, "y": self.y, "id": self.id,
               "height": self.height, "width": self.width}
        return dic

    @property
    def width(self):
        """get the value for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set a value for width attribute"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get a value for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set a value for height attribute"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the value for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """set a value for x attribute"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the value for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value for y attribute"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
