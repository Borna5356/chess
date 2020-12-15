"""
This module is responsible for
creating the different possible 
moves for the pieces

"""
import pieces
import board

def move_piece(piece, board):
    """
    This function is for moving knights

    """
    if (piece.get_name() == "knight"):
        moves = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
    elif (piece.get_name() == "king"):
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    current_position = piece.get_position()
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
                other_piece = current_board[new_row][new_col]
                if (piece.get_color() != other_piece.get_color()):
                    new_positions.append((new_row, new_col))
                else:
                    continue
        
    if (len(new_positions) == 0):
        return None
    else:
        new_position = input("Enter the position to move your knight to Ex.(2 3): ")
        new_position = new_position.split(' ')
        new_row = int(new_position[1])
        new_col = int(new_position[0])

        while ((new_row, new_col) not in new_positions):
            new_position = input("You can\'t move to that position. Try again Ex.(2 3): ")
            new_position = new_position.split(' ')
            new_row = int(new_position[1])
            new_col = int(new_position[0])
        return (new_row, new_col)

def move_pawn(pawn, board):
    """
    This function shows what moves
    a pawn can do

    """

    diagonal_black_moves = [(1, 1), (1, -1)]
    vertical_black_moves = [(1, 0)]
    diagonal_white_moves = [(-1, 1), (-1, -1)]
    vertical_white_moves = [(-1, 0)]

    if (pawn.get_color() == "black"):
        new_positions = find_positions(pawn, board, vertical_black_moves, diagonal_black_moves)

    else:
        new_positions = find_positions(pawn, board, vertical_white_moves, diagonal_white_moves)

    if (len(new_positions) == 0):
        return None
    else:
        new_position = input("Enter the position to move your pawn to Ex.(2 3): ")
        new_position = new_position.split(' ')
        new_row = int(new_position[1])
        new_col = int(new_position[0])
        
        while ((new_row, new_col) not in new_positions):
            new_position = input("You can\'t move to that position. Try again Ex.(2 3): ")
            new_position = new_position.split(' ')
            new_row = int(new_position[1])
            new_col = int(new_position[0])

        return (new_row, new_col)

def find_positions(pawn, board, vertical_moves, diagonal_moves):

    """
    decides the moves available
    for the pawn

    """
    new_positions = []
    current_position = pawn.get_position()
    chess_board = board.get_board()
    has_moved = pawn.get_has_moved()

    if (has_moved == False):
        if (pawn.get_color() == "black"):
            vertical_moves.append((2, 0))
        else:
            vertical_moves.append((-2, 0))
        pawn.set_has_moved()

    for move in vertical_moves:
        new_row = current_position[0] + move[0]
        new_col = current_position[1] + move[1]
        if (new_row < 0) or (new_row > 7) or (new_col < 0) or (new_col > 7):
            pass
        else:
            if (chess_board[new_row][new_col] == '-'):
                new_positions.append((new_row, new_col))
            else:
                break

    for move in diagonal_moves:
        new_row = current_position[0] + move[0]
        new_col = current_position[1] + move[1]
        if (new_row < 0) or (new_row > 7) or (new_col < 0) or (new_col > 7):
            continue
        else:
            if (chess_board[new_row][new_col] != '-'):
                other_piece = chess_board[new_row][new_col]
                if (pawn.get_color() != other_piece.get_color()):
                    new_positions.append((new_row, new_col))
                else:
                    pass
    return new_positions

def move_queen(queen, board):
    """
    This function is for moving the queen

    """
    current_board = board.get_board()
    current_position = queen.get_position()
    current_row = current_position[0]
    current_col = current_position[1]
    color = queen.get_color()
    while (True):
        new_position = input("Enter the position that you want to move the queen to Ex.(1 4): ")
        new_position = new_position.split(' ')
        new_row = int(new_position[1])
        new_col = int(new_position[0])
        change_in_row = new_row - current_row
        change_in_col = new_col - current_col
        if (abs(change_in_row) == abs(change_in_col)):
            is_valid = check_diagnol(current_board, current_position, change_in_row, change_in_col)
            if (is_valid == True):
                return (new_row, new_col)
            else:
                print("That is a not a valid move")
                continue
        elif (change_in_row != 0) and (change_in_col == 0):
            pass
        elif( change_in_col != 0) and (change_in_row == 0):
            pass
        else:
            print("That is not a valid move")
            continue

def check_diagnol(board, current_position, change_in_row, change_in_col):
    """
    checks if diagnol move is possible

    """
    if (change_in_row < 0):
        increment_row = -1
    else:
        increment_row = 1
    
    if (change_in_col < 0):
        increment_col = -1
    else:
        increment_col = 1
    
    current_row = current_position[0]
    current_col = current_position[1]
    for spaces_checked in range(abs(change_in_col)):
        new_row = current_row + increment_row * (spaces_checked + 1)
        new_col = current_col + increment_col * (spaces_checked + 1)
        if (is_space_empty(board, new_row, new_col)):
            continue
        else:
            return False
    return True

def is_space_empty(board, row, col):
    """
    checks to see if the space is empty

    """
    space = board[row][col]
    if (space == '-'):
        return True
    else:
        return False