EARLY_GAME = 36
MIDDLE_GAME = 75


class heuristic:

    def __init__(self, board):
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
        self._board = board
        self._color = None
        self._size = board.get_board_size()

    def nb_piece_heuristic(self):
        if self._color == self._board._WHITE:
            return self._board._WHITE - self._board._nbBLACK
        return self._board._nbBLACK - self._board._nbWHITE

    def weight_heuritic(self):
        result = 0
        for x in range(self._size):
            for y in range(self._size):
                if self._board._board[x][y] == self._color:
                    result += self._weight[x][y]
                elif self._board._board[x][y] == self._board._EMPTY:
                    pass
                else:
                    result -= self._weight[x][y]
 #       print("WEIGHT : ", result)
        return result

    # reduce opponent moves possibility
    def mobility_heuristic(self):
        opponentMoves = 0
        for x in range(self._size):
            for y in range(self._size):
                opponentMoves = opponentMoves + self._board.lazyTest_ValidMove(self._board._flip(self._color), x, y)

        opponentCorner = self.corner_number()

        result = - (10 * opponentCorner + opponentMoves)    # not sur about that
#        print("MOBILITY : ", result)
        return result

    def diff_heuristic(self):
        (nb_opponent_pieces, nb_player_pieces) = self._board.get_nb_pieces()
        result = nb_player_pieces - nb_opponent_pieces
        #print("DIFF : ", result)
        return result

    def corner_number(self):
        oColor = self._board._flip(self._color)
        result = 0
        if self._board._board[0][0] == oColor:
            result += 1
        if self._board._board[0][self._size - 1] == oColor:
            result += 1
        if self._board._board[self._size - 1][0] == oColor:
            result += 1
        if self._board._board[self._size - 1][self._size - 1] == oColor:
            result += 1
        return result

    def compute_all_heuristics(self):
        (opponent, player) = self._board.get_nb_pieces()
        pieces = opponent + player

        # use different heuristics depending on game phase
        if pieces <= EARLY_GAME:
            return self.weight_heuritic() + self.mobility_heuristic()
        elif pieces <= MIDDLE_GAME:
            return self.weight_heuritic() + 10*self.mobility_heuristic()  ##+ others
        else:
            return self.weight_heuritic() + 15*self.mobility_heuristic() + 200*self.diff_heuristic()
