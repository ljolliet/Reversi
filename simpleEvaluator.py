from evaluator import heuristicEvaluatorInterface
import heuristic


class simpleEvaluator(heuristicEvaluatorInterface):

    def __init__(self, board):
        self._board = board
        self._heuristic = heuristic.heuristic(self._board)

    def compute(self):
        return self._heuristic.compute_all_heuristics()
