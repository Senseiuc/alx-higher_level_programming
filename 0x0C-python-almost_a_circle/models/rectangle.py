#!/usr/bin/python3
"""creating a rectagle class"""
from models.base import Base

class Rectangle(Base):
    """
       A class that inherits from the rectangle class
       Attributes:
           __nb_objects(int): The number of int objects.
    """

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
           Initialise the rectangle class
           Args:
               width (int): the object id
               height (int): the height of the rectangle
               x (int): postion on the x axis
               y (int): position on the y axis
               id (int): the id of the object
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """ get the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """ set the value of the rectangle width"""
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Set/get the height of the Rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """Set/get the x coordinate of the Rectangle."""
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """Set/get the y coordinate of the Rectangle."""
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
