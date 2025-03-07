
#!/usr/bin/python3
"""
    define a class 'Square'
"""


class Square:
    """
    a class that defines square by its size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializing the size and position of square
        Args:
            size(int): size of the square
            position(tuple): position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        retrieves the position of square
        Returns:
            the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the position of square
        Args:
            value(tuple): new position of the square
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        returns the current square area
        Returns:
            the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square with # character using position
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for i in range(self.__position[1]):
            print()

        # Print square with horizontal offset
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

