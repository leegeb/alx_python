"""This represents a class square"""


class Square:
    """Assigns size to private instance and checks for integer and value for greater than 0"""

    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
