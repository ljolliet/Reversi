# -*- coding: utf-8 -*-

import time
import Reversi
from random import randint
from playerInterface import *

SIZE = 10
# noinspection PyAttributeOutsideInit
class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(SIZE)
        self._mycolor = None
        self._weight = [
            [4, -3, 2, 2, 2, 2, 2, 2, -3, 4],
            [-3, -4, -1, -1, -1, -1, -1, -1, -4, -3],
            [2, -1, 1, 0, 0, 0, 0, 1, -1, 2],
            [2, -1, 0, 1, 1, 1, 1, 0, -1, 2],
            [2, -1, 0, 1, 1, 1, 1, 0, -1, 2],
            [2, -1, 0, 1, 1, 1, 1, 0, -1, 2],
            [2, -1, 0, 1, 1, 1, 1, 0, -1, 2],
            [2, -1, 1, 0, 0, 0, 0, 1, -1, 2],
            [-3, -4, -1, -1, -1, -1, -1, -1, -4, -3],
            [4, -3, 2, 2, 2, 2, 2, 2, -3, 4]
        ]
        self._depth = 3

    def getPlayerName(self):
        return "Random Player"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1, -1)
        move = self.start_minmax(self._depth, True)
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

    def heuristic(self):
        result = 0
        for x in range(SIZE):
            for y in range(SIZE):
                if self._board._board[x][y] == self._board._BLACK:
                    result += self._weight[x][y]
                elif self._board._board[x][y] == self._board._WHITE:
                    result -= self._weight[x][y]
                else:
                    pass
        return result

    def minimax(self, depth, maximizingPlayer):
        if depth == 0 or self._board.is_game_over():
            return self.heuristic()
        if maximizingPlayer:
            value = -10000
            for m in self._board.legal_moves():
                self._board.push(m)
                value = max(value, self.minimax(depth - 1, False))
                self._board.pop()
            return value
        else:
            value = 10000
            for m in self._board.legal_moves():
                self._board.push(m)
                value = min(value, self.minimax(depth - 1, True))
                self._board.pop()
            return value

    def start_minmax(self, depth, maximizingPlayer):
        if self._board.is_game_over():
            return
        best_move = None
        if maximizingPlayer:
            best_value = -10000
            for m in self._board.legal_moves():
                self._board.push(m)
                value = self.minimax(depth - 1, not maximizingPlayer)
                if value > best_value:
                    best_value = value
                    best_move = m
                self._board.pop()
        else:
            best_value = 10000
            for m in self._board.legal_moves():
                self._board.push(m)
                value = self.minimax(depth - 1, not maximizingPlayer)
                if value < best_value:
                    best_value = value
                    best_move = m
                self._board.pop()
        return best_move
