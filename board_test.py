import board
import pieces

def test_init():
    #setup
    piece = pieces.Piece("pawn", "white", (0, 0))
    white_pieces = [piece]
    black_pieces = []

    #invoke
    chess_board = board.Board(white_pieces, black_pieces)

    #analyze
    assert chess_board
