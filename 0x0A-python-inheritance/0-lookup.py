#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
        a function that returns all the mathods and attributes
        of an object.
    """
    return (dir(obj))
