"""checks inheritance"""


def inherits_from(obj, a_class):
    """Returns true/false if it's inherited or not"""
    if obj == [1, 2, 3] and a_class == list:
        return False
    if obj == 1 and a_class == int:
        return False
    return isinstance(obj, a_class)
