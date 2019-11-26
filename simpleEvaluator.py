from evaluator import heuristicEvaluatorInterface
import heuristic

EARLY_GAME = 36
MIDDLE_GAME = 75
END_GAME = 95

class simpleEvaluator(heuristicEvaluatorInterface):

    def __init__(self, board):
        self._board = board
        self._heuristic = heuristic.heuristic(self._board)

    def compute(self):
        (opponent, player) = self._board.get_nb_pieces()
        pieces = opponent + player

        # use different heuristics depending on game phase
        if pieces <= EARLY_GAME:
            return self._heuristic.early_game_heuristics()
        elif pieces <= MIDDLE_GAME:
            return self._heuristic.middle_game_heuristics()
        elif pieces <= END_GAME:
            return self._heuristic.late_game_heuristics()
        else:
            return self._heuristic.end_game_heuristics()
        #return self._heuristic.compute_all_heuristics()
