"""
This module is responsible for
creating the different possible 
moves for the pieces

"""
import pieces
import board

def move_pawn(pawn):
    """
    This function shows what moves
    a pawn can do

    """
    if (pawn.get_color() == "black"):
        return (1, 0)
    else:
        return (-1, 0)
