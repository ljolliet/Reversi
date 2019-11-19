# -*- coding: utf-8 -*-

import time
import Reversi
from random import randint
from playerInterface import *


class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None

    def getPlayerName(self):
        return "Random Player"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1, -1)
        moves = [m for m in self._board.legal_moves()]
        move = moves[randint(0, len(moves) - 1)]
        self._board.push(move)
        print("I am playing ", move)
        (c, x, y) = move
        assert (c == self._mycolor)
        print("My current board :")
        print(self._board)
        return (x, y)

    def playOpponentMove(self, x, y):
        assert (self._board.is_valid_move(self._opponent, x, y))
        print("Opponent played ", (x, y))
        self._board.push([self._opponent, x, y])

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")


def heuristic(b):
    result = 0
    values = {"k": 200, "q": 9, "r": 5, "b": 3, "n": 3, "p": 1}
    for p in b.piece_map().values():
        s = p.symbol()
        if s.isupper():
            result += values.get(s.lower())
        else:
            result -= values.get(s)
    return result


def deroulementMinMax(b, player1=True):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    b.push(start_minmax(b, 3, player1))
    deroulementMinMax(b, not player1)
    b.pop()


def minimax(board, depth, maximizingPlayer):
    if depth == 0 or board.is_game_over():
        return heuristic(board)
    if maximizingPlayer:
        value = -10000
        for m in board.legal_moves:
            board.push(m)
            value = max(value, minimax(board, depth - 1, False))
            board.pop()
        return value
    else:
        value = 10000
        for m in board.legal_moves:
            board.push(m)
            value = min(value, minimax(board, depth - 1, True))
            board.pop()
        return value


def start_minmax(board, depth, maximizingPlayer):
    if board.is_game_over():
        return
    best_move = None
    if maximizingPlayer:
        best_value = -10000
        for m in board.legal_moves:
            board.push(m)
            value = minimax(board, depth - 1, not maximizingPlayer)
            if value > best_value:
                best_value = value
                best_move = m
                board.pop()
    else:
        best_value = 10000
        for m in board.legal_moves:
            board.push(m)
            value = minimax(board, depth - 1, not maximizingPlayer)
            if value < best_value:
                best_value = value
                best_move = m
                board.pop()
    return best_move
