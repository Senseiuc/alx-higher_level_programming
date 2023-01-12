#!/usr/bin/python3
"""
   A class that inherits the list object and also sorts a given list
"""


class MyList(list):
    """
        A subclass of list class that sorts the list
    """
    def print_sorted(self):
        """ print sorted list"""
        print(sorted(self))
