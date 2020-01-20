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
