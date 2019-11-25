# -*- coding: utf-8 -*-

import time
import Reversi
import heuristic
from random import randint
from playerInterface import *
import simpleEvaluator

SIZE = 10


# noinspection PyAttributeOutsideInit
class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(SIZE)
        self._mycolor = None
        self._heuristic = simpleEvaluator.simpleEvaluator(self._board)  # TODO at the end set the heuristic
        self._depth = 3

    def getPlayerName(self):
        return "Random Player"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1, -1)
        move = self.start_minmax(self._depth, True)
        print("MOVE ", move)
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
        self._heuristic._color = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")

    def setHeuristic(self, h):
        self._heuristic = h

    def minimax(self, depth, maximizingPlayer):
        if depth == 0 or self._board.is_game_over():
            return self._heuristic.compute()
        if maximizingPlayer:
            value = -100000000
            for m in self._board.legal_moves():
                self._board.push(m)
                value = max(value, self.minimax(depth - 1, False))
                self._board.pop()
            return value
        else:
            value = 100000000
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
            best_value = -100000000
            for m in self._board.legal_moves():
                self._board.push(m)
                value = self.minimax(depth - 1, not maximizingPlayer)
                if value > best_value:
                    best_value = value
                    best_move = m
                self._board.pop()
        else:
            best_value = 100000000
            for m in self._board.legal_moves():
                self._board.push(m)
                value = self.minimax(depth - 1, not maximizingPlayer)
                if value < best_value:
                    best_value = value
                    best_move = m
                self._board.pop()
        return best_move
