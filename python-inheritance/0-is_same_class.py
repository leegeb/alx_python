def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj (object): The object to be checked.
        a_class (type): The class to compare the object's type with.

    Returns:
        bool: True if the object is exactly an instance of the specified class; False otherwise.
    """
    return (type(obj) is a_class)
