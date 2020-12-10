"""
This handles the board of
the game

"""

import pieces, moves

class Board:
    """
    This class handles the board

    """
    __slots__ = ["__white_pieces", "__black_pieces", "__board"]

    def __init__(self, white_pieces, black_pieces):
        """
        initializes a board

        """
        self.__white_pieces = white_pieces
        self.__black_pieces = black_pieces
        self.__board = []

        for current_row in range(8):
            row = []
            for column in range(8):
                row.append('-')
            self.__board.append(row)

        for piece in self.__white_pieces:
            position = piece.get_position()
            row = position[0]
            column = position[1]
            self.__board[row][column] = piece

        for piece in self.__black_pieces:
            position = piece.get_position()
            self.__board[position[0]][position[1]] = piece
    
    def get_board(self):
        """
        This constructor returns the board

        """
        return self.__board

    def change_position(self, current_position, new_position):
        """
        Changes the position of the pieces on the board

        """
        current_row = current_position[0]
        current_col = current_position[1]
        new_row = new_position[0]
        new_col = new_position[1]
        piece = self.__board[current_row][current_col]
        self.__board[new_row][new_col] = piece
        self.__board[current_row][current_col] = '-'
        
    
    def print_board(self):
        """
        prints the chess board

        """
        print('  ', end = ' ')
        for num in range(8):
            print(num, end = '   ')
        print()
        for index in range(len(self.__board)):
            print(index, end = '  ')
            for position in self.__board[index]:
                if (position != '-'):
                    piece = position
                    if (piece.get_color() == "black"):

                        if (piece.get_shorthand() == "Kn"):
                            print("\033[34m" + piece.get_shorthand() + "\033[37m", end = '  ')
                        else:
                            print("\033[34m" + piece.get_shorthand() + "\033[37m", end = '   ')

                    else:
                        if (piece.get_shorthand() == "Kn"):
                            print(piece.get_shorthand(), end = '  ')
                        else:
                            print(piece.get_shorthand(), end = '   ')
                else:
                    print(position, end = '   ')
            print()

def setup():
    """
    This method sets up the board 
    for the game to begin

    """
    white_pieces = pieces.make_white_pieces()
    black_pieces = pieces.make_black_pieces()
    board = Board(white_pieces, black_pieces)
    return board

def main():
    white_pawn = pieces.Piece("pawn", "white", (6, 2), moves.move_pawn)
    white_pieces = [white_pawn]
    black_pawn = pieces.Piece("pawn", "black", (1, 2), moves.move_pawn)
    black_pieces = [black_pawn]
    chess_board = Board(white_pieces, black_pieces)
    chess_board.print_board()
    print()
    white_pawn.make_move(chess_board)
    chess_board.print_board()
    print()
    black_pawn.make_move(chess_board)
    chess_board.print_board()

if (__name__ == "__main__"):
    main()

