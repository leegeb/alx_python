"""function checks for instance of class of an object"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or if the object is a class that inherited from, the specific class"""
    return (isinstance(obj, a_class))
