"""function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """True if the object's class hierarchy includes a_class; False otherwise."""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
