#!/usr/bin/python3
"""a function that returns True if the object is
   an instance of a class that inherited (directly
   or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):

    """Check if an object is subclass of an
       instance of a given class or from inherited.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
