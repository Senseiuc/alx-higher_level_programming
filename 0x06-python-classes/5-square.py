#!/usr/bin/python3
""" a square class that returns nothing """


class Square:
    """ a square class
        Attributes: size
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square
            Args:
            Returns:
                An integer
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Draws the square using #
           Returns:Nothing
        """
        if self.__size > 0:
            print((("#"*self.__size)+"\n")*(self.__size-1), end='')
            print("#"*self.__size)
        else:
            print("\n")
