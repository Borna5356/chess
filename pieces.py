"""
This file handles the creation of
different pieces in chess

"""
class Piece:
    """
    This class handles the cretation of 
    different types of pieces

    """
    __slots__ = ["__name", "__color","__current_position", "__shorthand", "__moves"]

    def __init__(self, name, color, current_position, moves = 0):
        """
        initializes a piece

        """
        self.__name = name
        self.__color = color
        self.__current_position = current_position
        self.__shorthand = color[0].upper() + name[0].upper()
        self.__moves = moves
    
    def get_position(self):
        """
        gets the current position of the piece

        """
        return self.__current_position
    
    def get_shorthand(self):
        """
        gets the shorthand of the piece

        """
        return self.__shorthand