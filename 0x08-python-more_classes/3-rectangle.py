#!/usr/bin/python3
""" a rectangle class that returns nothing """


class Rectangle:
    """ a rectangle class
        Attributes:
            width(int): Width of the rectangle
            height(int): Height of the rectangle
    """
    def __init__(self, width=0, height=0):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Draws the square using #
           Returns:Nothing
        """
        if self.__width > 0 and self.__height > 0:
            tri_ini = ((("#"*self.__width)+"\n")*(self.__height-1))
            return tri_ini + ("#"*self.__width)
        else:
            return ""
