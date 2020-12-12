import pieces
import moves
import board
import io

def test_init():
    #setup none

    #invoke
    pawn = pieces.Piece("pawn", "White", (0, 0), None)

    #analyize
    assert pawn

def test_make_move_white(monkeypatch):
    #setup
    pawn = pieces.Piece("pawn", "white", (6, 2), moves.move_pawn)
    monkeypatch.setattr("sys.stdin", io.StringIO("2 5"))
    chess_board = board.Board([pawn], [])
    expected_position = (5, 2)

    #invoke
    pawn.move(chess_board)

    #analyze
    assert expected_position == pawn.get_position()

def test_make_move_black(monkeypatch):
    #setup
    pawn = pieces.Piece("pawn", "black", (1, 2), moves.move_pawn)
    monkeypatch.setattr("sys.stdin", io.StringIO("2 2"))
    chess_board = board.Board([], [pawn])
    expected_position = (2, 2)

    #invoke
    pawn.move(chess_board)

    #analyze
    assert expected_position == pawn.get_position()
