import moves
import board
import pieces
import io

def test_move_white_pawn(monkeypatch):
    #setup
    pawn = pieces.Piece("pawn", "white", (1, 0), moves.move_pawn)
    monkeypatch.setattr("sys.stdin",io.StringIO("0 0"))
    white_pieces = [pawn]
    chess_board = board.Board(white_pieces, [])
    expected = (0, 0)

    #invoke
    actual = moves.move_pawn(pawn, chess_board)

    #analyze
    assert expected == actual

def test_move_black_pawn(monkeypatch):
    #setup
    pawn = pieces.Piece("pawn", "black", (1, 0), moves.move_pawn)
    monkeypatch.setattr("sys.stdin",io.StringIO("0 2"))
    white_pieces = [pawn]
    chess_board = board.Board(white_pieces, [])
    expected = (2, 0)

    #invoke
    actual = moves.move_pawn(pawn, chess_board)

    #analyze
    assert expected == actual

def test_move_knight(monkeypatch):
    #setup
    monkeypatch.setattr("sys.stdin", io.StringIO("1 3"))
    knight = pieces.Piece("knight", "black", (1, 0), moves.move_piece)
    white_pieces = [knight]
    chess_board = board.Board(white_pieces, [])
    expected = (3, 1)

    #invoke
    actual = moves.move_piece(knight, chess_board)

    #analyze
    assert expected == actual