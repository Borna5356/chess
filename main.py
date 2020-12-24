"""
This is the main file for the game
of chess

"""
import pieces
import board
import player

def main():
    chess_board = board.setup()
    chess_board.print_board()
    while (True):
        while (True):
            piece = player.choose_piece(chess_board)
            if (piece == None):
                print("That is not a valid piece")
                continue

            elif (piece == False):
                return None
            else:
                move = piece.move(chess_board)
                if (move == True):
                    print()
                    chess_board.print_board()
                    break
                elif (move == None):
                    continue
                else:
                    print("You can\'t move that piece")
                    continue
    

if (__name__ == "__main__"):
    main()
    