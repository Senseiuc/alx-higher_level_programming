#!/usr/bin/python3
class LockedClass:
    """ A class that prevents creation of attributes
        except for first name
        Attributes:
            first_name (str): the only attribute allowed
    """
    __slots__ = ['first_name']
