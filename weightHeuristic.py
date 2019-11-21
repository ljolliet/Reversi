from heuristicInterface import *


class weightHeuristic(heuristicInterface):

    def __init__(self):
        self._weight = [
            [100, -20, 20, 10, 5, 5, 10, 20, -20, 100],
            [-20, -50, -2, -2, -2, -2, -2, -2, -50, -20],
            [20, -2, -1, -1, -1, -1, -1, -1, -2, 20],
            [10, -2, -1, -1, -1, -1, -1, -1, -2, 10],
            [5, -2, -1, -1, -1, -1, -1, -1, -2, 5],
            [5, -2, -1, -1, -1, -1, -1, -1, -2, 5],
            [10, -2, -1, -1, -1, -1, -1, -1, -2, 10],
            [20, -2, -1, -1, -1, -1, -1, -1, -2, 20],
            [-20, -50, -2, -2, -2, -2, -2, -2, -50, -20],
            [100, -20, 20, 10, 5, 5, 10, 20, -20, 100]
        ]
        self._size = 10

    def compute(self, board, color):
        result = 0
        for x in range(self._size):
            for y in range(self._size):
                if board._board[x][y] == color:
                    result += self._weight[x][y]
                elif board._board[x][y] == board._EMPTY:
                    pass
                else:
                    result -= self._weight[x][y]
        return result
