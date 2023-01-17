#!/usr/bin/python3
"""creating a base class"""


class Base:
    """
       A class base
       Attributes:
           __nb_objects(int): The number of int objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
           Initialise the base class
           Args:
               id (int): the object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
