#!/usr/bin/python3
""" a square class that returns nothing """


class Square:
    """ a square class
        Attributes: size
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
	elif type(position[0]) != int || type(position[1] != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 || position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
            print("\n"*self.__position[1], end='')
            pos = '_'*self.__position[0]
            sq = "#"*self.__size
            print((pos+sq+"\n")*(self.__size-1), end='')
            print('_'*self.__position[0]+"#"*self.__size)
        else:
            print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
