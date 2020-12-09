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
    for count in range(2):
        piece = player.choose_piece(chess_board)
        piece.make_move(chess_board)
        chess_board.print_board()
    

if (__name__ == "__main__"):
    main()
    