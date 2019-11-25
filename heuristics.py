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
        opponentMoves = 0
        for x in range(0, self._size - 1):
            for y in range(0, self._size - 1):
                opponentMoves = self._board.lazyTest_ValidMove(self._board._flip(self._color), x, y)


        # Verify if it's possible to play in a corner and how many move are possible for the current player
        #playerCorner = self.corner_number()
        #possibleMovePlayer = len(self._board.legal_moves())

        opponentCorner = self.corner_number()

        # result = 10*(playerCorner - opponentCorner) + ((possibleMovePlayer - possibleMoveOpponen)/(possibleMovePlayer + possibleMoveOpponen))

        result = - (10 * opponentCorner + opponentMoves)
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
        pieces = self._board._nbWHITE + self._board._nbBLACK
        max_pieces = self._size * self._size
        EARLY_GAME = max_pieces/3
        MIDDLE_GAME = (max_pieces/3) * 2

        #print("WEIGHT VALUE", self.weight_heuritic)
        #print("MOBILITY VALUE", self.mobily_heuritic)
        #print("NB_PIECE VALUE", self.nb_piece_heuristic)

        #use differents heuristics depend of number of move in the game (game time)
        if pieces < EARLY_GAME:
            return self.weight_heuritic() + self.nb_piece_heuristic()
        elif pieces < MIDDLE_GAME:
            return self.weight_heuritic() + self.mobility_heuristic() + self.nb_piece_heuristic()
        else:
            return self.weight_heuritic() + self.mobility_heuristic() + self.nb_piece_heuristic()


