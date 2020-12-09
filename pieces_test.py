import pieces, moves

def test_init():
    #setup none

    #invoke
    pawn = pieces.Piece("pawn", "White", (0, 0))

    #analyize
    assert pawn

def test_make_move():
    #setup
    pawn = pieces.Piece("pawn", "white", (6, 2), moves.move_pawn)
    expected_position = (5, 2)

    #invoke
    pawn.make_move()

    #analyze
    assert expected_position == pawn.get_position()
