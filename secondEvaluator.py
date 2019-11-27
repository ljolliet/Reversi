from evaluator import heuristicEvaluatorInterface
import heuristic

EARLY_GAME = 36
MIDDLE_GAME = 75
END_GAME = 95


class secondEvaluator(heuristicEvaluatorInterface):

    def __init__(self, board):
        self._board = board
        self._heuristic = heuristic.heuristic(self._board)

    def compute(self):
        (opponent, player) = self._board.get_nb_pieces()
        pieces = opponent + player
        if pieces <= EARLY_GAME:
            return 1000 * self._heuristic.corners_v2() + 50 * self._heuristic.mobility_v2()
        elif pieces <= MIDDLE_GAME:
            return 1000 * self._heuristic.corners_v2() + 20 * self._heuristic.mobility_v2() + 10 * self._heuristic.diff_v2() + 100 * self._heuristic.parity()
        else:
            return 1000 * self._heuristic.corners_v2() + 100 * self._heuristic.mobility_v2() + 500 * self._heuristic.diff_v2() + 500 * self._heuristic.parity()
