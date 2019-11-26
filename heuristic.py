EARLY_GAME = 36
MIDDLE_GAME = 75


class heuristic:

    def __init__(self, board):
        self._size = board.get_board_size()
        self._weight = [
            [200, -100, 100, 50, 50, 50, 50, 100, -100, 200],
            [-100, -200, -50, -50, -50, -50, - 50, -50, -200, -100],
            [100, -50, 100, 0, 0, 0, 0, 100, -50, 100],
            [50, -50, 0, 0, 0, 0, 0, 0, -50, 50],
            [50, -50, 0, 0, 0, 0, 0, 0, -50, 50],
            [50, -50, 0, 0, 0, 0, 0, 0, -50, 50],
            [50, -50, 0, 0, 0, 0, 0, 0, -50, 50],
            [100, -50, 100, 0, 0, 0, 0, 100, -50, 100],
            [-100, -200, -50, -50, -50, -50, - 50, -50, -200, -100],
            [200, -100, 100, 50, 50, 50, 50, 100, -100, 200],
        ]
        self._corners = [
            [0, 0],
            [0, self._size - 1],
            [self._size - 1, 0],
            [self._size - 1, self._size - 1]
        ]

        self._board = board
        self._color = None

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
        # print("WEIGHT : ", result)
        return result

    # reduce opponent moves possibility
    def mobility_heuristic(self):
        opponentMoves = 0
        for x in range(self._size):
            for y in range(self._size):
                opponentMoves = opponentMoves + self._board.lazyTest_ValidMove(self._board._flip(self._color), x, y)

        # opponentCorner = self.corner_number()

        # result = - (10 * opponentCorner + opponentMoves)    # not sur about that
        #        print("MOBILITY : ", opponentMoves)
        return opponentMoves

    def diff_heuristic(self):
        (nb_opponent_pieces, nb_player_pieces) = self._board.get_nb_pieces()
        result = nb_player_pieces - nb_opponent_pieces
        # print("DIFF : ", result)

        return result

    def corner_heuristic(self):
        color = self._color
        oColor = self._board._flip(self._color)
        result = 0

        for x in range(len(self._corners)):
            for y in range(2):
                if self._board._board[x][y] == color:
                    result += 1
                elif self._board._board[x][y] == oColor:
                    result -= 1
        # print("result = ", result)
        return result

    def compute_all_heuristics(self):
        (opponent, player) = self._board.get_nb_pieces()
        pieces = opponent + player

        # use different heuristics depending on game phase
        if pieces <= EARLY_GAME:
            weight = self.weight_heuritic()
            mobility = self.mobility_heuristic()
            result = weight + mobility
            print("early game :\nweight : ", weight, " result: ", result)
            return result
        elif pieces <= MIDDLE_GAME:
            result = self.weight_heuritic() + 100 * self.mobility_heuristic() + 1000 * self.corner_heuristic()  ##+ others
            print("mid game : ", result)
            return result
        else:
            result = self.weight_heuritic() + 150 * self.mobility_heuristic() + 200 * self.diff_heuristic() + 1000 * self.corner_heuristic()
            print("late game : ", result)
            return result

    def early_game_heuristics(self):
        weight = self.weight_heuritic()
        mobility = 10 * self.mobility_heuristic()
        corner = 2000 * self.corner_heuristic()
        return weight + mobility + corner

    def middle_game_heuristics(self):
        weight = self.weight_heuritic()
        mobility = 20 * self.mobility_heuristic()
        corner = 2000 * self.corner_heuristic()
        return weight + mobility + corner

    def late_game_heuristics(self):
        weight = self.weight_heuritic()
        mobility = 150 * self.mobility_heuristic()
        diff = 200 * self.diff_heuristic()
        corner = 2000 * self.corner_heuristic()
        return weight + mobility + diff + corner

    def end_game_heuristics(self):
        return self.diff_heuristic()
