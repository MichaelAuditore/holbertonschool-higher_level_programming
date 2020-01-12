#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Say_my_name function prints the first and lastname.

    Parameters:
              first_name (String): represents a String with the first name
              last_name (String): represents a String with the last name


    TypeErrors:
              first_name must be a string
              last_name must be a string

    Returns:
           Not return, only print the parameters in a specific format
    """
    if first_name is None or type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if last_name is None or type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
