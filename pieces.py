"""
This file handles the creation of
different pieces in chess

"""
class Piece:
    """
    This class handles the cretation of 
    different types of pieces

    """
    __slots__ = ["__name", "__color","__current_position", "__shorthand"]

    def __init__(self, name, color, current_position):
        """
        initializes a piece

        """
        self.__name = name
        self.__color = color
        self.__current_position = current_position
        self.__shorthand = color[0] + name[0]