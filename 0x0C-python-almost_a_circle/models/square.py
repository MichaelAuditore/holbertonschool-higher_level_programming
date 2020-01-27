#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the class Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return String representation of object"""
        s = "[Square] ("
        s += str(self.id) + ") "
        s += str(self.x) + "/" + str(self.y)
        s += " - " + str(self.width)
        return (s)

    def update(self, *args, **kwargs):
        """Update attributes for an Square object"""
        if (len(args) > 0):
            attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of object"""
        dic = {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
        return dic

    @property
    def size(self):
        """get the value for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """set a value for size attribute"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
