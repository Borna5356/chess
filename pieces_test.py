import pieces, moves, board

def test_init():
    #setup none

    #invoke
    pawn = pieces.Piece("pawn", "White", (0, 0), None)

    #analyize
    assert pawn

def test_make_move_white():
    #setup
    pawn = pieces.Piece("pawn", "white", (6, 2), moves.move_pawn)
    chess_board = board.Board([pawn], [])
    expected_position = (5, 2)

    #invoke
    pawn.make_move(chess_board)

    #analyze
    assert expected_position == pawn.get_position()

def test_make_move_black():
    #setup
    pawn = pieces.Piece("pawn", "black", (1, 2), moves.move_pawn)
    chess_board = board.Board([], [pawn])
    expected_position = (2, 2)

    #invoke
    pawn.make_move(chess_board)

    #analyze
    assert expected_position == pawn.get_position()
