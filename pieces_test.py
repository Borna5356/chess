import pieces

def test_init():
    #setup none

    #invoke
    pawn = pieces.Piece("pawn", "White", (0, 0), "moves forward 1 square")

    #analyize
    assert pawn