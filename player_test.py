import player
import pieces
import board
import moves
import io

def test_choose_piece(monkeypatch):
    #setup
    monkeypatch.setattr("sys.stdin", io.StringIO("0,0"))
    piece = pieces.Piece("pawn", "white", (0, 0), moves.move_pawn)
    white_pieces = [piece]
    black_pieces = []
    chess_board = board.Board(white_pieces, black_pieces)
    
    #invoke
    result = player.choose_piece(chess_board)

    #analyze
    assert piece == result