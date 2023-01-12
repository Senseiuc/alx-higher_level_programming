#!/usr/bin/python3
"""A function that checks if two objects
   are of the same class or inherited class
"""


def is_kind_of_class(obj, a_class):

    """Check if an object is exactly an
       instance of a given class or from inherited.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return isinstance(obj, a_class)
