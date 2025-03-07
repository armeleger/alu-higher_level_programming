#!/usr/bin/python3
"""
    define a class 'Square'
"""


class Square:
    """
    a class that defines square by its size
    """
    def __init__(self, size=0):
        """
        initializing the size of square
        Args:
            size(int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        retrieves the size of square
        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of square
        Args:
            value(int): new size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the current square area
        Returns:
            the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square with # character
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
