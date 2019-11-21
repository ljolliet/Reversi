# -*- coding: utf-8 -*-

import time
import Reversi
from random import randint
from playerInterface import *
from heuristicInterface import *

SIZE = 10


# noinspection PyAttributeOutsideInit
class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(SIZE)
        self._mycolor = None
        self._heuristic = None  # TODO at the end set the heuristic
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

    def setHeuristic(self, heuristic):
        self._heuristic = heuristic

    def mobility_heuristic(self):
        result = 0
        color = self._mycolor
        playerCorner = self.corner_number(self._mycolor)
        opponentCorner = self.corner_number(self._board._flip(self._mycolor))
        # possibleMovePlayer =
        # possibleMoveOpponen =
        print("mobility heuristic")
        # result = 10*(playerCorner - opponentCorner) + ((possibleMovePlayer - possibleMoveOpponen)/(possibleMovePlayer + possibleMoveOpponen))
        print(result)
        return result

    def corner_number(self, color):
        result = 0
        if self._board._board[0][0] == color:
            result += 1
        if self._board._board[0][SIZE - 1] == color:
            result += 1
        if self._board._board[SIZE - 1][0] == color:
            result += 1
        if self._board._board[SIZE - 1][SIZE - 1] == color:
            result += 1
        return result

    def minimax(self, depth, maximizingPlayer):
        if depth == 0 or self._board.is_game_over():
            return self._heuristic.compute(self._board, self._mycolor)
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
