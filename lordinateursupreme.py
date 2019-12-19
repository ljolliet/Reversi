# -*- coding: utf-8 -*-

import time
import Reversi
import sys
import random
from playerInterface import *

class myPlayer(PlayerInterface):

    weights = [[100,-80,30,30,30,30,30,30,-80,100],
                    [-80,-100,-40,-40,-40,-40,-40,-40,-100,-80],
                    [30,-40,20,10,10,10,10,20,-40,30],
                    [30,-40,10,-20,0,0,-20,10,-40,30],
                    [30,-40,10,0,10,10,0,10,-40,30],
                    [30,-40,10,0,10,10,0,10,-40,30],
                    [30,-40,10,-20,0,0,-20,10,-40,30],
                    [30,-40,20,10,10,10,10,20,-40,30],
                    [-80,-100,-40,-40,-40,-40,-40,-40,-100,-80],
                    [100,-80,30,30,30,30,30,30,-80,100]]

    # - Stable : Cannot be flipped at any point of the game
    # - Semi-stable : Cannot be flipped next turn
    # - Unstable : Could be flipped next turn
    def stabilityHeuristic(self):
        res = 0
        for i in range(self._board.get_board_size()):
            for j in range(self._board.get_board_size()):
                if self._board._board[i][j] != self._board._EMPTY:
                    if self.canBeFlippedNextTurn(i,j):
                        res = res + 1
                    elif self.cannotBeFlipped(i,j):
                        res = res + 10
                    else:
                        res = res + 4         
        return (res / self._maxSH) * 100

    def maxStabilityHeuristic(self):
        res = 0
        for i in range(self._board.get_board_size()):
            for j in range(self._board.get_board_size()):
                res = res + 10
        return res
    #   _ _       _ _
    # _ X X     _ O X
    # _ X X     _ X X
    #   
    #   --> OK    --> NOT OK
    # o
    #  o  == DIAG 1
    #   o
    def cannotBeFlipped(self, i, j):
        return self.leftTopLocked(i,j) or self.leftBotLocked(i,j) or self.rightTopLocked(i,j) or self.rightBotLocked(i,j)

    def leftTopLocked(self, i, j):
        return self.isNoneLineBefore(i,j) and self.isNoneColBefore(i,j) and self.isNoneDiag1Before(i,j)

    def leftBotLocked(self, i, j):
        return self.isNoneLineBefore(i,j) and self.isNoneColAfter(i,j) and self.isNoneDiag2Before(i,j)
    
    def rightTopLocked(self, i, j):
        return self.isNoneLineAfter(i,j) and self.isNoneColBefore(i,j) and self.isNoneDiag2After(i,j)

    def rightBotLocked(self, i, j):
        return self.isNoneLineAfter(i,j) and self.isNoneColAfter(i,j) and self.isNoneDiag1After(i,j)

    def isNoneLineBefore(self, i, j):
        res = True
        while i > 0:
            i = i - 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return False
        return res

    def isNoneLineAfter(self,i ,j):
        res = True
        while i < self._board.get_board_size() - 1:
            i = i + 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return False
        return res

    def isNoneColBefore(self, i, j):
        res = True
        while j > 0:
            j = j - 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return False
        return res

    def isNoneColAfter(self,i ,j):
        res = True
        while j < self._board.get_board_size() - 1:
            j = j + 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return False
        return res

    def isNoneDiag1Before(self, i, j):
        res = True
        while i > 0 and j > 0:
            j = j - 1
            i = i - 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return False
        return res

    def isNoneDiag1After(self,i ,j):
        res = True
        while i < self._board.get_board_size() - 1 and j < self._board.get_board_size() - 1:
            j = j + 1
            i = i + 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return False
        return res

    def isNoneDiag2Before(self, i, j):
        res = True
        while i > 0 and j < self._board.get_board_size() - 1:
            j = j + 1
            i = i - 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return False
        return res

    def isNoneDiag2After(self,i ,j):
        res = True
        while i < self._board.get_board_size() - 1 and j > 0:
            j = j - 1
            i = i + 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return False
        return res

    def canBeFlippedNextTurn(self, i, j):
        return self.canBeFlippedLine(i,j) or self.canBeFlippedCol(i,j) or self.canBeFlippedDiag(i,j)

    def canBeFlippedLine(self, i, j):
        if self.isOpponentLineBefore(i,j) and self.isOpponentLineAfter(i,j):
            return False
        if (not self.isOpponentLineBefore(i,j)) and (not self.isOpponentLineAfter(i,j)):
            return False
        return True

    def canBeFlippedCol(self, i, j):
        if self.isOpponentColBefore(i,j) and self.isOpponentColAfter(i,j):
            return False
        if (not self.isOpponentColBefore(i,j)) and (not self.isOpponentColAfter(i,j)):
            return False
        return True

    def canBeFlippedDiag(self, i, j):
        if self.isOpponentDiag1Before(i,j) and self.isOpponentDiag1After(i,j):
            return False
        if (not self.isOpponentDiag1Before(i,j)) and (not self.isOpponentDiag1After(i,j)):
            return False
        if self.isOpponentDiag2Before(i,j) and self.isOpponentDiag2After(i,j):
            return False
        if (not self.isOpponentDiag2Before(i,j)) and (not self.isOpponentDiag2After(i,j)):
            return False
        return True

    def isOpponentLineBefore(self, i, j):
        res = False
        while i > 0:
            i = i - 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return True
        return res

    def isOpponentLineAfter(self, i, j):
        res = False
        while i < self._board.get_board_size() - 1:
            i = i + 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return True
        return res

    def isOpponentColBefore(self, i, j):
        res = False
        while j > 0:
            j = j - 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return True
        return res

    def isOpponentColAfter(self, i, j):
        res = False
        while j < self._board.get_board_size() - 1:
            j = j + 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return True
        return res

    def isOpponentDiag1Before(self, i, j):
        res = False
        while i > 0 and j > 0:
            j = j - 1
            i = i - 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return True
        return res

    def isOpponentDiag1After(self, i, j):
        res = False
        while i < self._board.get_board_size() - 1 and j < self._board.get_board_size() - 1:
            j = j + 1
            i = i + 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return True
        return res    

    def isOpponentDiag2Before(self, i, j):
        res = False
        while i > 0 and j < self._board.get_board_size() - 1:
            j = j + 1
            i = i - 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return True
        return res

    def isOpponentDiag2After(self, i, j):
        res = False
        while i < self._board.get_board_size() - 1 and j > 0:
            j = j - 1
            i = i + 1
            if self._board._board[i][j] == self._board._EMPTY:
                return False
            if self._board._board[i][j] == self._opponent:
                return True
        return res  

    def weightsHeuristic(self):
        res = 0
        for i in range(self._board.get_board_size()):
            for j in range(self._board.get_board_size()):
                if self._board._board[i][j] == self._mycolor:
                    res = res + self.weights[i][j]
                elif self._board._board[i][j] == self._opponent:
                    res = res - self.weights[i][j]   
        return (res / self._maxWH) * 100

    def maxWeightsHeuristic(self):
        res = 0
        for i in range(self._board.get_board_size()):
            for j in range(self._board.get_board_size()):
                res = res + abs(self.weights[i][j])
        return res


    def parityHeuristic(self):
        res = 0
        for i in range(self._board.get_board_size()):
            for j in range(self._board.get_board_size()):
                if self._board._board[i][j] == self._mycolor:
                    res = res + 1
                elif self._board._board[i][j] == self._opponent:
                    res = res - 1
        return res / 100

    def cornersHeuristic(self):
        res = 0
        if self._board._board[0][0] == self._mycolor:
            res = res + 25
        elif self._board._board[0][0] == self._opponent:
            res = res - 25
        if self._board._board[0][self._board.get_board_size() - 1] == self._mycolor:
            res = res + 25
        elif self._board._board[0][self._board.get_board_size() - 1] == self._opponent:
            res = res - 25
        if self._board._board[self._board.get_board_size() - 1][0] == self._mycolor:
            res = res + 25
        elif self._board._board[self._board.get_board_size() - 1][0] == self._opponent:
            res = res - 25
        if self._board._board[self._board.get_board_size() - 1][self._board.get_board_size() - 1] == self._mycolor:
            res = res + 25
        elif self._board._board[self._board.get_board_size() - 1][self._board.get_board_size() - 1] == self._opponent:
            res = res - 25
        return res

    def heuristics(self):
        wh = self.weightsHeuristic()
        sh = self.stabilityHeuristic()
        ph = self.parityHeuristic()
        ch = self.cornersHeuristic()

        if self._numTurn < 20:
            return wh + 0.5 * sh + 3 * ph + 3 * ch
        elif self._numTurn > 60:
            return wh + 3 * sh + ph + 3 * ch
        return wh + 2 * sh + ph + 3 * ch

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None
        self._maxSH = self.maxStabilityHeuristic()
        self._maxWH = self.maxWeightsHeuristic()
        self._numTurn = 0

    def getPlayerName(self):
        return "Superman"

    def minimax2(self, turn, depth, depthMax, alpha, beta):
        if self._board.is_game_over():
            (nbwhites, nbblacks) = self._board.get_nb_pieces()
            if nbwhites > nbblacks:
                if self._mycolor == self._board._WHITE:
                    return (sys.maxsize, None)
                else:
                    return (-sys.maxsize - 1, None)
            else:
                if self._mycolor == self._board._WHITE:
                    return (-sys.maxsize - 1, None)
                else:
                    return (sys.maxsize, None)
        if depth + 1 == depthMax:
            return (self.heuristics(), None)
        if turn == 1:
            #our turn
            bestEval = -sys.maxsize - 1
            bestMove = []
            moves = [m for m in self._board.legal_moves()]
            for move in moves:
                self._board.push(move)
                (evalMove, evaluatedMove) = self.minimax2(0, depth + 1, depthMax, alpha, beta)
                #alphabeta
                #if alpha > evalMove:
                #    alpha = evalMove
                #if alpha >= beta:
                #    self._board.pop()
                #    return (alpha, evaluatedMove)
                #    
                if evalMove > bestEval:
                    bestEval = evalMove
                    bestMove = [move]
                elif evalMove == bestEval:
                    bestMove.append(move)
                self._board.pop()
            return (bestEval, random.choice(bestMove))
        elif turn == 0:
            #opponent turn
            worstEval = sys.maxsize
            worstMove = []
            moves = [m for m in self._board.legal_moves()]
            for move in moves:
                self._board.push(move)
                (evalMove, evaluatedMove) = self.minimax2(1, depth + 1, depthMax, alpha, beta)
                #alphabeta
                #if beta < evalMove:
                #    beta = evalMove
                #if beta >= alpha:
                #    self._board.pop()
                #    return (beta, evaluatedMove) 
                #
                if evalMove < worstEval:
                    worstEval = evalMove
                    worstMove = [move]
                elif evalMove == worstEval:
                    worstMove.append(move)
                self._board.pop()
            return (worstEval, random.choice(worstMove))

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1,-1)
        (evalMove, move) = self.minimax2(1,0,4, -sys.maxsize - 1, sys.maxsize)
        self._board.push(move)
        (c,x,y) = move
        assert(c==self._mycolor)
        print("My current board :")
        print(self._board)
        self._numTurn = self._numTurn + 1
        return (x,y) 

    def playOpponentMove(self, x,y):
        assert(self._board.is_valid_move(self._opponent, x, y))
        print("Opponent played ", (x,y))
        self._board.push([self._opponent, x, y])
        self._numTurn = self._numTurn + 1

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")



