"""creation of an empty class"""


class BaseGeometry:
    """the empty class"""

    def __dir__(self):
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != "__init_subclass__":
                n_attributes.append(attr)
        return n_attributes

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
