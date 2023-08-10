class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square's sides (private).

    Methods:
        __init__(self, size=0): Constructor method for initializing the square.
        area(self): Calculates and returns the area of the square.
        size(self): Property getter to retrieve the size of the square.
        size(self, value): Property setter to set the size of the square.
        my_print(self): Prints the square using '#' characters.
    """
    
    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size (int, optional): The size of the square's sides. Defaults to 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
    
    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square's sides.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value
    
    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Prints the square using '#' characters.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        
        for _ in range(self.__size):
            print("#" * self.__size)
