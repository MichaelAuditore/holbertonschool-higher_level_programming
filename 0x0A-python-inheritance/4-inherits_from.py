#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    defines if an object is an instance and have the same type
    of another class
    """
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return (True)
    return False
