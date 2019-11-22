class heuristicsdef:

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
        return result

    def mobility_heuristic(self):
        #color = self._mycolor

        # Verify if it's possible to play in a corner and how many move are possible for the current player
        playerCorner = self.corner_number()
        possibleMovePlayer = len(self._board.legal_moves())

        # opponentCorner = self.corner_number(self._board._flip(color))
        # possibleMoveOpponen = len(self._board.legal_moves())
        # print(possibleMoveOpponen)

        # result = 10*(playerCorner - opponentCorner) + ((possibleMovePlayer - possibleMoveOpponen)/(possibleMovePlayer + possibleMoveOpponen))

        result = 10 * playerCorner + possibleMovePlayer
        return result

    def corner_number(self):
        result = 0
        if self._board._board[0][0] == self._color:
            result += 1
        if self._board._board[0][self._size - 1] == self._color:
            result += 1
        if self._board._board[self._size - 1][0] == self._color:
            result += 1
        if self._board._board[self._size - 1][self._size - 1] == self._color:
            result += 1
        return result

    def compute_all_heuristics(self):
        pieces = self._board._nbWHITE + self._board._nbBLACK
        max_pieces = self._size * self._size
        EARLY_GAME = max_pieces/3
        MIDDLE_GAME = (max_pieces/3) * 2

        #use differents heuristics depend of number of move in the game (game time)
        if pieces < EARLY_GAME:
            return self.weight_heuritic() * self.nb_piece_heuristic()
        elif pieces < MIDDLE_GAME:
            return self.weight_heuritic() * (0.5 * self.mobility_heuristic()) * (2*self.nb_piece_heuristic())
        else:
            return self.weight_heuritic() * self.mobility_heuristic() * (5*self.nb_piece_heuristic())
