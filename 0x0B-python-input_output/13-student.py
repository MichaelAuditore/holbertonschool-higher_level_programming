#!/usr/bin/python3


class Student:
    """
    Class to define a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        d = {}
        if type(attrs) is not list:
            return (self.__dict__)
        else:
            obj = self.__dict__
            for at in attrs:
                for key in obj:
                    if key == at:
                        d[at] = self.__dict__[at]
            return (d)

    def reload_from_json(self, json):
        obj = self.__dict__
        for key in json:
            for keyobj in obj:
                if key == keyobj:
                    setattr(self, key, json[key])
