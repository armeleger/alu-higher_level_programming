#!/usr/bin/python3
# a class that defines square
"""
   define a square
"""


class Square:
    """
       square with a private instance called size
    """
    def __init__(self, size):
        """
        Args:
            size(int): size of the square
        """
        self.__size = size
