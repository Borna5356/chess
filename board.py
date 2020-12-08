import pieces
"""
This handles the board of
the game

"""
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
                    if (piece.get_shorthand() == "Kn"):
                        print(piece.get_shorthand(), end = '  ')
                    else:
                        print(piece.get_shorthand(), end = '   ')
                else:
                    print(position, end = '   ')
            print()
    
def main():
    piece = pieces.Piece("pawn", "white", (3, 4))
    other_piece = pieces.Piece("knight", "white", (1, 2))
    white_pieces = [piece, other_piece]
    board = Board(white_pieces, [])
    board.print_board()

if (__name__ == "__main__"):
    main()

