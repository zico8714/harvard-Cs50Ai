"""
Tic Tac Toe Player
"""

import math
import copy
import sys
import random
from typing import Counter
import numpy as np

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    oCount = 0
    xCount = 0 

    for listed in board:
        for element in listed:
            if element == X:
                xCount += 1
            if element == O:
                oCount += 1

    if oCount < xCount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    setOfActions = set()
    tup = ()
    for listed, num in enumerate(board):
        for element, name in enumerate(num):
            if name == EMPTY:
                tup = (listed, element)
                setOfActions.add(tup)
    if setOfActions == set():
        return "Game ended"
    return setOfActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    copiaBarata = copy.deepcopy(board)
    move1, move2 = action
    if copiaBarata[move1][move2] != EMPTY:
        raise NameError("asd")
    copiaBarata[move1][move2] = player(board)
    return copiaBarata

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    diagonal1 = []
    diagonal2 =[]
    column = []

    def check(lista):
        xCount = 0
        oCount = 0
        for i in lista:
            if i == X:
                xCount += 1
            if i == O:
                oCount += 1
        if xCount == 3:
            return X
        if oCount == 3:
            return O
    
    for rows in board:
        retorno = check(rows)
        if retorno is not None:
            return retorno

    for i in range(3):
        diagonal1.append(board[i][i])
    retorno = check(diagonal1)
    if retorno is not None:
        return retorno
    diagonal1 = []

    for j in range(3):
        k = 2 - j
        diagonal2.append(board[j][k])
    retorno = check(diagonal2)
    if retorno is not None:
        return retorno
    diagonal2 = []

    for i in range(3):
        for j in range(3):     
            column.append(board[j][i])
        retorno = check(column)
        if retorno is not None:
            return retorno
        column = []

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        win = winner(board)
        if win == X:
            return 1
        elif win == O:
            return -1
        else:
            return 0

def minimax(board):
    """Return the optimal move for the AI to do"""
    if terminal(board):
        return None
    if player(board) == X:
        for action in actions(board):
            disaster1 = Minimo(result(board, action))
            if disaster1 != -1:
                return action
            
    else:
        for action in actions(board):
            disaster = Maximo(result(board, action))
            if disaster != 1:
                return action
        

            
            
        

def Maximo(board):
    if terminal(board):
        return utility(board)
    value = -10000
    for action in actions(board):
        value = max(value, Minimo(result(board, action)))
    return value

def Minimo(board):
    if terminal(board):
        return utility(board)
    value = 10000
    for action in actions(board):
        value = min(value, Maximo(result(board, action)))
    return value