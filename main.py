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
    for moves in range(5):
        while (True):
            piece = player.choose_piece(chess_board)
            if (piece.move(chess_board)):
                print()
                chess_board.print_board()
                break
            else:
                print("You can\'t move that piece")
                continue
    

if (__name__ == "__main__"):
    main()
    