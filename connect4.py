import numpy as np


# def main():
# board=create_board()
# print(board)

def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece():
    pass


def is_vaild_loacation(board, col):
    pass


def get_next_open_row():
    pass


board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    # ask for Player 1  input

    if turn == 0:

        col = int(input("Player 1 make your seclection (0-6);"))

        ## ask for Player 2 input

    else:
        col = int(input("Player 2 make your seclection (0-6);"))

    turn += 1
    turn = turn % 2
