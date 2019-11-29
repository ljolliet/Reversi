from evaluator import heuristicEvaluatorInterface
import heuristic

EARLY_GAME = 31
MIDDLE_GAME = 91


class secondEvaluator(heuristicEvaluatorInterface):

    def __init__(self, board):
        self._board = board
        self._heuristic = heuristic.heuristic(self._board)

    def compute(self):
        (opponent, player) = self._board.get_nb_pieces()
        pieces = opponent + player
        if pieces <= EARLY_GAME:
            corners = 1000 * self._heuristic.corners_v2()
            mobility = 50 * self._heuristic.mobility_v2()
            return corners + mobility
        elif pieces <= MIDDLE_GAME:
            corners = 1000 * self._heuristic.corners_v2()
            mobility = 20 * self._heuristic.mobility_v2()
            diff = 10 * self._heuristic.diff_v2()
            parity = 100 * self._heuristic.parity()
            return corners + mobility + diff + parity
        else:
            return 1000 * self._heuristic.corners_v2() + 100 * self._heuristic.mobility_v2() + 500 * self._heuristic.diff_v2() + 500 * self._heuristic.parity()

    def setColor(self, color):
        self._heuristic._color = color
