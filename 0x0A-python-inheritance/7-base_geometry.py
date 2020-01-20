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
