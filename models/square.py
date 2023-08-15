"""imports the Rectangle class from base file"""
from models.rectangle import Rectangle
"""this is a class that has all the info about square"""


class Square(Rectangle):
    """this class holds all the attributes of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        if not (type(size) == int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

        """getter method for size"""
    @property
    def size(self):
        """returns the value of size"""
        return self.width
    """setter method for size"""
    @size.setter
    def size(self, value):
        """sets the value of size"""
        if not (type(value) == int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
