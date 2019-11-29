# -*- coding: utf-8 -*-

import time
import Reversi
import heuristic
from random import randint
from playerInterface import *
import simpleEvaluator
import secondEvaluator

SIZE = 10
MIDDLE_GAME = 75
END_GAME = 85
INF = 1000000


# noinspection PyAttributeOutsideInit
class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(SIZE)
        self._color = None
        self._heuristic = secondEvaluator.secondEvaluator(self._board)  # TODO at the end set the heuristic
        self._depth = 3

    def getPlayerName(self):
        return "Random Player"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1, -1)
        move = self.start_alphaBeta()
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
        self._heuristic.setColor(color)
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")

    def setHeuristic(self, h):
        self._heuristic = h

    def alphaBeta(self, depth, maximizingPlayer, alpha, beta):
        if depth == 0 or self._board.is_game_over():
            result = self._heuristic.compute()
            return result
        if maximizingPlayer:
            value = -INF
            for m in self._board.legal_moves():
                self._board.push(m)
                result = self.alphaBeta(depth - 1, False, alpha, beta)
                value = max(value, result)
                alpha = max(alpha, value)
                self._board.pop()
                if alpha >= beta:
                    break
        else:
            value = INF
            for m in self._board.legal_moves():
                self._board.push(m)
                result = self.alphaBeta(depth - 1, True, alpha, beta)
                value = min(value, result)
                beta = min(beta, value)
                self._board.pop()
                if alpha >= beta:
                    break
        return value

    def start_alphaBeta(self):
        if self._board.is_game_over():
            return
        best_move = None
        best_value = -INF
        for m in self._board.legal_moves():
            self._board.push(m)
            value = self.alphaBeta(self._depth - 1, False, -INF, +INF)
            if value > best_value:
                best_value = value
                best_move = m
            self._board.pop()

        print('\x1b[6;30;42m' + 'Best move : ' + str(best_value) + '\x1b[0m')
        return best_move

    def minimax(self, depth, maximizingPlayer):
        if depth == 0 or self._board.is_game_over():
            """(opponent, player) = self._board.get_nb_pieces()
            pieces = opponent + player
            if pieces > END_GAME:
                self._depth = 5
            if pieces > MIDDLE_GAME:
                self._depth = 4"""
            return self._heuristic.compute()
        if maximizingPlayer:
            value = -INF
            for m in self._board.legal_moves():
                self._board.push(m)
                value = max(value, self.minimax(depth - 1, False))
                self._board.pop()
            return value
        else:
            value = INF
            for m in self._board.legal_moves():
                self._board.push(m)
                value = min(value, self.minimax(depth - 1, True))
                self._board.pop()
            return value

    def start_minmax(self):
        if self._board.is_game_over():
            return
        best_move = None
        best_value = -INF
        for m in self._board.legal_moves():
            self._board.push(m)
            value = self.minimax(self._depth - 1, False)
            if value > best_value:
                best_value = value
                best_move = m
            self._board.pop()
        print('\x1b[6;30;42m' + 'Best move : ' + str(best_value) + '\x1b[0m')
        return best_move
