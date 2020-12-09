"""
This is the main file for the game
of chess

"""
import pieces
import board

def main():
    chess_board = board.setup()
    chess_board.print_board()

if (__name__ == "__main__"):
    main()
    