import Reversi

import openingBook
from playerInterface import *
import myEvaluator

SIZE = 10
EARLY_GAME = SIZE * SIZE / 3
MIDDLE_GAME = SIZE * SIZE * 2 / 3
INF = 1000000


# noinspection PyAttributeOutsideInit
class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(SIZE)
        self._color = None
        self._evaluator = myEvaluator.myEvaluator(self._board)
        self._openingBook = openingBook.OpeningBook()
        self._depth = 3

    def getPlayerName(self):
        return "Quick Player"

    def getPlayerMove(self):
        # self.updateDepth()
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return -1, -1

        opening_move = self._openingBook.getNextMove()
        if opening_move is not None:
            print('\x1b[6;30;41m' + 'Opening move : ' + '\x1b[0m')
            move = opening_move
        else:
            tmp_move_corner = self.cornerMove()
            tmp_move_kill = self.blockMove()
            if tmp_move_corner is not None:
                print('\x1b[6;30;41m' + 'Quick move : ' + '\x1b[0m')
                move = tmp_move_corner
            if tmp_move_kill is not None:
                print('\x1b[6;30;41m' + 'Block move : ' + '\x1b[0m')
                move = tmp_move_kill
            else:
                move = self.start_alphaBeta()
        print("MOVE ", move)
        self._board.push(move)
        print("I am playing ", move)
        (c, x, y) = move
        assert (c == self._mycolor)
        print("My current board :")
        print(self._board)
        return x, y

    def playOpponentMove(self, x, y):
        assert (self._board.is_valid_move(self._opponent, x, y))
        print("Opponent played ", (x, y))
        self._openingBook.addOponnentMove(x, y)
        self._board.push([self._opponent, x, y])

    def newGame(self, color):
        self._mycolor = color
        self._evaluator.setColor(color)
        self._openingBook.setColor(color)
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")

    def setHeuristic(self, h):
        self._evaluator = h

    def alphaBeta(self, depth, maximizingPlayer, alpha, beta):
        if depth == 0 or self._board.is_game_over():
            result = self._evaluator.compute()
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

    def cornerMove(self):
        for x, y in self._evaluator.getCorners():
            if self._board.is_valid_move(self._mycolor, x, y):
                return [self._mycolor, x, y]
        return None

    def blockMove(self):
        for move in self._board.legal_moves():
            self._board.push(move)
            if len(self._board.legal_moves()) == 1:
                oColor = self._board._flip(self._mycolor)
                if self._board.legal_moves()[0] == [oColor, -1, -1]:
                    self._board.pop()
                    return move
            self._board.pop()
        return None

    def blockPlayer(self):
        oColor = self._board._flip(self._mycolor)
        # return not self._board.at_least_one_legal_move(oColor)
        return False    

    def updateDepth(self):
        (opponent, player) = self._board.get_nb_pieces()
        pieces = opponent + player
        if pieces > EARLY_GAME and pieces < MIDDLE_GAME:
            print('\x1b[6;30;43m' + 'DEPTH 4' + '\x1b[0m')
            self._depth = 4
        elif pieces > MIDDLE_GAME:
            print('\x1b[6;30;43m' + 'DEPTH 5' + '\x1b[0m')
            self._depth = 5
