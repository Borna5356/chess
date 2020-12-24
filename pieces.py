"""
This file handles the creation of
different pieces in chess

"""
import moves, board

class Piece:
    """
    This class handles the cretation of 
    different types of pieces

    """
    __slots__ = ["__name", "__color","__current_position", "__shorthand", "__move_func", "__has_moved"]

    def __init__(self, name, color, current_position, move_func):
        """
        initializes a piece

        """
        self.__name = name
        self.__color = color
        self.__current_position = current_position
        if (name.capitalize() == "Knight"):
            self.__shorthand = name[0].upper() + name[1].lower()
        else:
            self.__shorthand = name[0].upper()
        self.__move_func = move_func
        self.__has_moved = False
    
    def get_name(self):
        """
        returns the name of the instance

        """
        return self.__name
    
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
    
    def get_color(self):
        """
        returns the color of the 
        piece

        """
        return self.__color

    def get_has_moved(self):
        """
        This constructor gets the
        value for has_moved field
        and return it
        
        """
        return self.__has_moved
    
    def set_has_moved(self):
        """
        sets the has_moved field
        to True

        """
        self.__has_moved = True
    
    def move(self, board):
        """
        This method moves the piece
        from one position to another

        """
        current_row = self.__current_position[0]
        current_col = self.__current_position[1]
        new_position = self.__move_func(self, board)
        if (new_position == None):
            return None
        elif (new_position == False):
            return False
        else:
            new_row = (new_position[0])
            new_col = (new_position[1])
            board.change_position(self.__current_position, (new_row, new_col))
            self.__current_position = (new_row, new_col)
            return True

def make_white_pieces():
    """
    This functions creates the white pieces
    for the game

    """
    white_pieces = []
    for col_num in range(8):
        pawn = Piece("pawn", "white", (6, col_num), moves.move_pawn)
        white_pieces.append(pawn)

    for col_num in range(0, 8, 7):
        rook = Piece("rook", "white", (7, col_num), moves.move_rook)
        white_pieces.append(rook)

    for col_num in range(1, 7, 5):
        knight = Piece("knight", "white", (7, col_num), moves.move_piece)
        white_pieces.append(knight)

    for col_num in range(2, 6, 3):
        bishop = Piece("bishop", "white", (7, col_num), moves.move_bishop)
        white_pieces.append(bishop)

    king = Piece("king", "white", (7, 3), moves.move_piece)
    queen = Piece("queen", "white", (7,4), moves.move_queen)
    white_pieces.append(king)
    white_pieces.append(queen)
    return white_pieces

def make_black_pieces():
    """
    This functions creates the white pieces
    for the game

    """
    black_pieces = []
    for col_num in range(8):
        pawn = Piece("pawn", "black", (1, col_num), moves.move_pawn)
        black_pieces.append(pawn)

    for col_num in range(0, 8, 7):
        rook = Piece("rook", "black", (0, col_num), moves.move_rook)
        black_pieces.append(rook)

    for col_num in range(1, 7, 5):
        knight = Piece("knight", "black", (0, col_num), moves.move_piece)
        black_pieces.append(knight)

    for col_num in range(2, 6, 3):
        bishop = Piece("bishop", "black", (0, col_num), moves.move_bishop)
        black_pieces.append(bishop)

    king = Piece("king", "black", (0, 3), moves.move_piece)
    queen = Piece("queen", "black", (0, 4), moves.move_queen)
    black_pieces.append(king)
    black_pieces.append(queen)
    return black_pieces

