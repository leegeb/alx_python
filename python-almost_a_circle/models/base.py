"""this is the base class for our project"""


class Base:
    """this class assigns the id a value"""
    __nb_objects = 0

    def __init__(self, id=None):
        if not id == None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
