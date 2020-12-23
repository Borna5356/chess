import board, pieces

def choose_piece(chess_board):
        """
        This function chooses a piece
        to move
        """
        position = input("Choose a piece to play using coordinates Ex.(0 1): ")
        position = position.split(' ')
        row = int(position[1])
        column = int(position[0])
        if (0 <= row <= 7) and (0 <= column <= 7):
                piece = chess_board.get_board()[row][column]
                if (piece == '-'):
                        return None
                else:
                        return piece
        else:
                return None