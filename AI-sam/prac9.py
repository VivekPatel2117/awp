# Importing all necessary libraries
import numpy as np
import random
from time import sleep

# Creates an empty board
def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

# Check for empty places on board
def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

# Select a random place for the player
def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board

# Checks whether the player has three marks in a vertical column
def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                break
        if win:
            return True
    return False

# Checks whether the player has three marks in a horizontal row
def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                break
        if win:
            return True
    return False

# Checks whether the player has three marks diagonally
def diag_win(board, player):
    win = True
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
            break
    if win:
        return True

    win = True
    for x in range(len(board)):
        if board[x, len(board) - 1 - x] != player:
            win = False
            break
    return win

# Evaluates whether there is a winner or tie
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1  # Tie
    return winner

# Main game loop
def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"\nBoard after player {player}'s move:")
            print(board)
            sleep(1)
            winner = evaluate(board)
            if winner != 0:
                break
    if winner == -1:
        print("\nIt's a tie!")
    else:
        print(f"\nPlayer {winner} wins!")

# Run the game
play_game()
