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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns the current square area
        """
        return self.__size ** 2
