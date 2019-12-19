from evaluator import heuristicEvaluatorInterface
import heuristic

EARLY_GAME = 31
MIDDLE_GAME = 91


class myEvaluator(heuristicEvaluatorInterface):

    def __init__(self, board):
        self._board = board
        self._heuristic = heuristic.heuristic(self._board)

    def compute(self):
        (opponent, player) = self._board.get_nb_pieces()
        pieces = opponent + player
        if pieces <= EARLY_GAME:
            mobility = 50 * self._heuristic.mobility_v2()
            corners = 1000 * self._heuristic.corners_v2()
            stability = 50 * self._heuristic.stability()
            return mobility + corners
        elif pieces <= MIDDLE_GAME:
            mobility = 20 * self._heuristic.mobility_v2()
            corners = 1000 * self._heuristic.corners_v2()
            diff = 10 * self._heuristic.diff_v2()
            parity = 100 * self._heuristic.parity()
            stability = 100 * self._heuristic.stability()
            return mobility + corners + diff + parity + stability
        else:
            mobility = 100 * self._heuristic.mobility_v2()
            corners = 1000 * self._heuristic.corners_v2()
            diff = 500 * self._heuristic.diff_v2()
            parity = 500 * self._heuristic.parity()
            stability = 500 * self._heuristic.stability()
            return mobility + corners + diff + parity + stability

    def setColor(self, color):
        self._heuristic._color = color

    def getCorners(self):
        return self._heuristic._corners

    def setBoard(self, board):
        self._heuristic.setBoard(board)

    def getInfo(self):
        return "contains stability"
