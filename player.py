import board, pieces

def choose_piece(chess_board, color):
        """
        This function chooses a piece
        to move
        """
        position = input("Choose a piece to play using coordinates Ex.(0 1): ")
        if (position == "stop"):
                return False
        else:
                position = position.split(' ')
                row = int(position[1])
                column = int(position[0])
                if (0 <= row <= 7) and (0 <= column <= 7):
                        piece = chess_board.get_board()[row][column]
                        if (piece == '-'):
                                print("That is not a valid piece")
                                return None
                        elif (piece.get_color() != color):
                                print("The color of the piece should be", color, "but was", piece.get_color())
                                return None
                        else:
                                return piece
                else:
                        return None