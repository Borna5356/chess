"""
This module is responsible for
creating the different possible 
moves for the pieces

"""
import pieces
import board

def move_pawn(pawn, board):
    """
    This function shows what moves
    a pawn can do

    """
    current_position = pawn.get_position()
    if (pawn.get_color() == "black"):
        new_row = current_position[0] + 1
        new_col = current_position[1] + 0
        return (new_row, new_col)
    else:
        new_row = current_position[0] - 1
        new_col = current_position[1] + 0
        return (new_row, new_col)

def move_knight(knight, board):
    """
    This function is for moving knights

    """
    moves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    current_position = knight.get_position()
    new_positions = []
    current_board = board.get_board()

    for index in range(len(moves)):
        move = moves[index]
        new_row = current_position[0] + move[0]
        new_col = current_position[1] + move[1]

        if (new_row < 0) or (new_row > 7) or (new_col < 0) or (new_col > 7):
            continue
        else:

            if (current_board[new_row][new_col] == '-'):
                new_positions.append((new_row, new_col))
            else:
                continue

    new_position = input("Enter the position to move your knight to Ex.(2 3): ")
    new_position = new_position.split(' ')
    new_row = int(new_position[1])
    new_col = int(new_position[0])

    while ((new_row, new_col) not in new_positions):
        new_position = input("You can\'t move to that location. Try again Ex.(2 3): ")
        new_position = new_position.split(' ')
        new_row = int(new_position[1])
        new_col = int(new_position[0])
    return (new_row, new_col)
    
