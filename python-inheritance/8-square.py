"""removes the __init__subclass__"""


class ExcludeInitSubclassMeta(type):
    """Remove __init_subclass__"""
    def __dir__(cls):
        attributes = super().__dir__()
        return [attr for attr in attributes if attr != "__init_subclass__"]


"""empty class"""


class BaseGeometry(metaclass=ExcludeInitSubclassMeta):
    """Empty class with __init_subclass__ removed"""

    def __dir__(self):
        original_attrs = super().__dir__()
        return [attr for attr in original_attrs if attr != "__init_subclass__"]

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        """class that takes in width and height"""


class Rectangle(BaseGeometry, metaclass=ExcludeInitSubclassMeta):
    """class that takes in width and height and validates it"""

    def __init__(self, width, height):
        """the init function"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        return (self.__width*self.__height)


"""class square"""


class Square(Rectangle, metaclass=ExcludeInitSubclassMeta):
    """This class contains all the info about a square"""

    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        """Calculates the area of a square"""
        return self.__size**2
