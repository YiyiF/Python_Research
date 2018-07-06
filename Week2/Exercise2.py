# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 21:28:18 2018

@author: eleve
"""

import numpy as np

def create_board():
    return np.zeros ((3,3))
    
board = create_board()


def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        
        
board = create_board()
place(board, 1, (0,0))


def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))
    
print(possibilities(board))


import random

def random_place(board, player):
    selection = possibilities(board)
    position = random.choice(selection)
    board[position] = player


#E5
board = create_board()

for rep in range(3):
    for player in [1, 2]:
        random_place(board, player)
print(board)


#E6 row_win
def row_win(board, player):
    for row in range(3):
        if all(board[row,] == np.ones(3)*player):
            return True
    return False
row_win(board, 1)

#E7 col_win
def col_win(board, player):
    for col in range(3):
        if all(board[: , col] == np.ones(3)*player):
            return True
    return False

col_win(board, 1)

# diag_win
cur = []
for row in range(3):
    cur.append(board[row, row])

def diag_win(board, player):
    mdiag = []
    ndiag = []
    for row in range(3):
        mdiag.append(board[row, row])
        ndiag.append(board[2-row, row])
    if all(mdiag == np.ones(3)*player) or all(ndiag == np.ones(3)*player):
        return True
    return False

diag_win(board, 1)


# E9
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if np.any(np.array([row_win(board, player),col_win(board, player),diag_win(board, player)])):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)

# E10
# play_game
#循环 是否棋盘满
#未满：下棋 先1 判断winner 否 2 判断winner 否

def play_game():
    board = create_board()
    while np.any(board == 0):
        for player in [1, 2]:
            random_place(board, player)
            result = evaluate(board)
            if result != 0:
                return result



# E11
import matplotlib.pyplot as plt
import time
start = time.time()
result = []
for i in range(1000):
    result.append(play_game())
end = time.time()
print(end - start)
plt.hist(result)
plt.show()


def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

play_strategic_game() 


import time
start = time.time()
result = []
for i in range(1000):
    result.append(play_strategic_game())
end = time.time()
print(end - start)
plt.hist(result)
plt.show()













