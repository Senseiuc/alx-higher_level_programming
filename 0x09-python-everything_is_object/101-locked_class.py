#!/usr/bin/python3
class LockedClass:
    """ A class that prevents creation of attributes
        except for first name
    """
    __slots__ = ['first_name']
