#!/usr/bin/python3
class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square's sides (private).

    Methods:
        __init__(self, size): Constructor method for initializing the square.
    """
    
    def __init__(self, size):
        """
        Initializes a square with the given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size
