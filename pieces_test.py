import pieces

def test_init():
    #setup none

    #invoke
    pawn = pieces.Piece("Pawn", "White", (0, 0))

    #analyize
    assert pawn