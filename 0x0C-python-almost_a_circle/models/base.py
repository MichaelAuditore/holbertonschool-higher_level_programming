#!/usr/bin/python3
import json


class Base:
    """
    Class that defines an object Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        js = "[]"
        if list_dictionaries is not None:
            js = json.dumps(list_dictionaries)
        return js

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        ls = []
        with open(filename, "w") as f:
            for obj in list_objs:
                ls.append(obj.to_dictionary())
            js = Base.to_json_string(ls)
            f.write(js)
        f.closed

    @staticmethod
    def from_json_string(json_string):
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        from os import path
        filename = cls.__name__ + ".json"
        ls = []
        if path.isfile(filename):
            with open(filename, "r") as f:
                for line in f:
                    js = Base.from_json_string(line)
                    for item in js:
                        ls.append(cls.create(**item))
        return (ls)
