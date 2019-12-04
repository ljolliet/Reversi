from evaluator import heuristicEvaluatorInterface
import heuristic

EARLY_GAME = 31
MIDDLE_GAME = 91


class seattleEvaluator(heuristicEvaluatorInterface):

    def __init__(self, board):
        self._board = board
        self._heuristic = heuristic.heuristic(self._board)

    def compute(self):
        (opponent, player) = self._board.get_nb_pieces()
        pieces = opponent + player
        if pieces <= EARLY_GAME:
            mobility = self._heuristic.mobility_v3()
            corners = self._heuristic.corners_v3()
            return mobility + corners
        elif pieces <= MIDDLE_GAME:
            mobility = self._heuristic.mobility_v3()
            corners = self._heuristic.corners_v3()
            diff = 10 * self._heuristic.diff_v2()
            parity = 100 * self._heuristic.parity()
            return mobility + corners + diff + parity
        else:
            mobility = self._heuristic.mobility_v3()
            corners = self._heuristic.corners_v3()
            diff = 10 * self._heuristic.diff_v2()
            parity = 100 * self._heuristic.parity()
            return mobility + corners + diff + parity

    def setColor(self, color):
        self._heuristic._color = color

    def getCorners(self):
        return self._heuristic._corners
