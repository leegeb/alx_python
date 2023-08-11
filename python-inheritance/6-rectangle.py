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

        """class takes width and height"""


class Rectangle(BaseGeometry):
    """Class that represents a rectangle"""

    def __init__(self, width, height):
        """Initialize width and height attributes"""
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)


r = Rectangle(3, 5)
print(r)
print(dir(r))
try:
    print("Rectangle: {} - {}".format(r.__width, r.__height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
