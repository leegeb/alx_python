"""removes the __init__subclass__"""


class ExcludeInitSubclassMeta(type):
    """Remove __init_subclass__"""
    def __dir__(cls):
        attributes = super().__dir__()
        return [attr for attr in attributes if attr != "__init_subclass__"]


"""empty class"""


class BaseGeometry(metaclass=ExcludeInitSubclassMeta):
    """Empty class with __init_subclass__ removed"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def __init_subclass__(cls):
        pass


class Rectangle(BaseGeometry):
    """Class that represents a rectangle"""

    def __init__(self, width, height):
        """Initialize width and height attributes"""
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """Return a string representation of the object"""
        return f"Rectangle: {self.__width} - {self.__height}"
