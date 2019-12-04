EARLY_GAME = 36
MIDDLE_GAME = 75


class heuristic:

    def __init__(self, board):
        self._size = board.get_board_size()
        self._weight = [
            [200, -100, 100, 50, 50, 50, 50, 100, -100, 200],
            [-100, -200, -50, -50, -50, -50, - 50, -50, -200, -100],
            [100, -50, 100, 0, 20, 20, 0, 100, -50, 100],
            [50, -50, 0, 0, 0, 0, 0, 0, -50, 50],
            [50, -50, 20, 0, 0, 0, 0, 20, -50, 50],
            [50, -50, 20, 0, 0, 0, 0, 20, -50, 50],
            [50, -50, 0, 0, 0, 0, 0, 0, -50, 50],
            [100, -50, 100, 20, 20, 0, 0, 100, -50, 100],
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

    def diff_v2(self):
        (whites, blacks) = self._board.get_nb_pieces()
        if self._color == self._board._BLACK:
            nb_player_pieces = blacks
            nb_opponent_pieces = whites
        else:
            nb_player_pieces = whites
            nb_opponent_pieces = blacks
        result = 100 * (nb_player_pieces - nb_opponent_pieces) / (nb_player_pieces + nb_opponent_pieces)
        return result

    def mobility_v2(self):
        opponentMoves = 0
        myMoves = 0
        for x in range(self._size):
            for y in range(self._size):
                if self._board.is_valid_move(self._board._flip(self._color), x, y):
                    opponentMoves += 1
                if self._board.is_valid_move(self._color, x, y):
                    myMoves += 1

        result = 100 * (myMoves - opponentMoves) / (myMoves + opponentMoves + 1)
        # idée : si le nombre d'opponentMoves est de 0, favoriser grandement le coup

        # if opponentMoves != 0:
        # result = 100 * (myMoves - opponentMoves) / (myMoves + opponentMoves + 1)
        # else:
        # result = 150 * (myMoves - opponentMoves) / (myMoves + opponentMoves + 1)
        return result

    def corners_v2(self):
        oColor = self._board._flip(self._color)
        myCorners = opponnentCorners = 0
        for x, y in self._corners:
            if self._board._board[x][y] == self._color:
                myCorners += 1
            elif self._board._board[x][y] == oColor:
                opponnentCorners += 1
        result = 100 * (myCorners - opponnentCorners) / (myCorners + opponnentCorners + 1)
        return result

    def parity(self):
        (opponent, player) = self._board.get_nb_pieces()
        pieces = opponent + player
        rest = self._size * self._size - pieces
        result = rest % 2 == 0 and -1 or 1
        return result

    def parity_v2(self):
        (opponent, player) = self._board.get_nb_pieces()
        return 100 * (player - opponent) / (player + opponent)
