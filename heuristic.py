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


    def mobility_calculation(self):
        opponentMoves = 0
        myMoves = 0
        for x in range(self._size):
            for y in range(self._size):
                if self._board.is_valid_move(self._board._flip(self._color), x, y):
                    opponentMoves += 1
                if self._board.is_valid_move(self._color, x, y):
                    myMoves += 1
        return myMoves, opponentMoves

    def mobility_v2(self):
        (myMoves, opponentMoves) = self.mobility_calculation()
        result = 100 * (myMoves - opponentMoves) / (myMoves + opponentMoves + 1)
        return result

    def mobility_v3(self):
        (myMoves, opponentMoves) = self.mobility_calculation()
        if myMoves + opponentMoves is not 0:
            return 100 * (myMoves - opponentMoves) / (myMoves + opponentMoves)
        else:
            return 0

    def corners_calculation(self):
        oColor = self._board._flip(self._color)
        myCorners = opponnentCorners = 0
        for x, y in self._corners:
            if self._board._board[x][y] == self._color:
                myCorners += 1
            elif self._board._board[x][y] == oColor:
                opponnentCorners += 1
        return myCorners, opponnentCorners

    def corners_v2(self):
        (myCorners, opponnentCorners) = self.corners_calculation()
        result = 100 * (myCorners - opponnentCorners) / (myCorners + opponnentCorners + 1)
        return result

    def corners_v3(self):
        (myCorners, opponnentCorners) = self.corners_calculation()
        if myCorners + opponnentCorners is not 0:
            return 100 * (myCorners - opponnentCorners) / (myCorners + opponnentCorners)
        else:
            return 0

    def parity(self):
        (opponent, player) = self._board.get_nb_pieces()
        pieces = opponent + player
        rest = self._size * self._size - pieces
        result = rest % 2 == 0 and -1 or 1
        return result

    def parity_v2(self):
        (opponent, player) = self._board.get_nb_pieces()
        return 100 * (player - opponent) / (player + opponent)

    def ligneStableHorizontale(self, pieceX, pieceY, color):
        if pieceX == 0 or pieceX == self._size -1:
            return True
        y = pieceY
        lineFull = 0
        halfLineUnicolorLeft = 0
        halfLineUnicolorRight = 0
        for x in range(self._size):
            case = self._board._board[x][y]
            if case != self._board._EMPTY:
                lineFull = lineFull + 1
            if x <= pieceX:
                if case == color:
                    halfLineUnicolorLeft = halfLineUnicolorLeft + 1
            else:
                if case == color:
                    halfLineUnicolorRight = halfLineUnicolorRight + 1
        if (lineFull == self._size - 1) or (halfLineUnicolorLeft == pieceX + 1) or (halfLineUnicolorRight == self._size - pieceX):
            return True
        return False

    def ligneStableVerticale(self, pieceX, pieceY, color):
        if pieceY == 0 or pieceY == self._size -1:
            return True
        x = pieceX
        lineFull = 0
        halfLineUnicolorTop = 0
        halfLineUnicolorDown = 0
        for y in range(self._size):
            case = self._board._board[x][y]
            if case != self._board._EMPTY:
                lineFull = lineFull + 1
            if y <= pieceY:
                if case == color:
                    halfLineUnicolorTop = halfLineUnicolorTop + 1
            else:
                if case == color:
                    halfLineUnicolorDown = halfLineUnicolorDown + 1
        if (lineFull == self._size - 1) or (halfLineUnicolorTop == pieceX + 1) or (halfLineUnicolorDown == self._size - pieceX):
            return True
        return False

    def diagoStableDownTop(self, pieceX, pieceY, color):
        if pieceX == 0 or pieceX == self._size - 1 or pieceY == 0 or pieceY == self._size -1:
            return True
        diagoDownTopFull = 1 #count the current piece
        halfDiagoLeft = 0
        halfDiagoRight = 0
        diagoSize = 0
        halfDiagoLeftSize = 0
        halfDiagoRightSize = 0

        x = pieceX
        y = pieceY

        while (x + 1 < self._size - 1) and (y - 1 >= 0):
            case = self._board._board[x][y]
            if case != self._board._EMPTY:
                diagoDownTopFull = diagoDownTopFull + 1
                if case == color:
                    halfDiagoLeft = halfDiagoLeft + 1
            diagoSize = diagoSize + 1
            halfDiagoLeftSize = halfDiagoLeftSize + 1
            x = x + 1
            y = y - 1

        x = pieceX
        y = pieceY

        while (x - 1 >= 0) and (y + 1 < self._size):
            case = self._board._board[x ][y]
            if case != self._board._EMPTY:
                diagoDownTopFull = diagoDownTopFull + 1
                if case == color:
                    halfDiagoRight = halfDiagoRight + 1
            diagoSize = diagoSize + 1
            halfDiagoRightSize = halfDiagoRightSize + 1
            x = x - 1
            y = y + 1

        if (diagoDownTopFull == diagoSize) or (halfDiagoRight == halfDiagoRightSize) \
                or (halfDiagoLeft == halfDiagoLeftSize):
            return True
        return False

    def diagoStableTopDown(self, pieceX, pieceY, color):
        if pieceX == 0 or pieceX == self._size - 1 or pieceY == 0 or pieceY == self._size - 1:
            return True
        diagoTopDownFull = 1  # count the current piece
        halfDiagoTop = 0
        halfDiagoDown = 0
        diagoSize = 0
        halfDiagoTopSize = 0
        halfDiagoDownSize = 0

        x = pieceX
        y = pieceY

        while (x - 1 >= 0) and (y - 1 >= 0):
            case = self._board._board[x - 1][y - 1]
            if case != self._board._EMPTY:
                diagoTopDownFull = diagoTopDownFull + 1
                if case == color:
                    halfDiagoTop = halfDiagoTop + 1
            x = x - 1
            y = y - 1
            diagoSize = diagoSize + 1
            halfDiagoTopSize = halfDiagoTopSize + 1

        x = pieceX
        y = pieceY

        while (x + 1 < self._size) and (y + 1 < self._size):
            case = self._board._board[x + 1][y + 1]
            if case != self._board._EMPTY:
                diagoTopDownFull = diagoTopDownFull + 1
                if case == color:
                    halfDiagoDown = halfDiagoDown + 1
            x = x + 1
            y = y + 1
            diagoSize = diagoSize + 1
            halfDiagoDownSize = halfDiagoDownSize + 1

        if (diagoTopDownFull == diagoSize) or (halfDiagoDown == halfDiagoDownSize) \
                or (halfDiagoTop == halfDiagoTopSize):
            return True
        return False






    def stability(self):
        myStability = 0
        opponnentStability = 0
        horizontalStable = False
        verticalStable = False
        firstDiagoStable = False
        secondDiagoStable = False

        for x in range(self._size):
            for y in range(self._size):
                if self._board._board[x][y] != self._board._EMPTY:
                    if self._board._board[x][y] == self._color:
                        horizontalStable = self.ligneStableHorizontale(x, y, self._color)
                        verticalStable = self.ligneStableVerticale(x, y, self._color)
                        firstDiagoStable = self.diagoStableDownTop(x, y, self._color)
                        secondDiagoStable = self.diagoStableTopDown(x, y, self._color)

                        if horizontalStable and verticalStable and firstDiagoStable and secondDiagoStable:
                            myStability = myStability + 1
                    else:
                        horizontalStable = self.ligneStableHorizontale(x, y, self._board._flip(self._color))
                        verticalStable = self.ligneStableVerticale(x, y, self._board._flip(self._color))
                        firstDiagoStable = self.diagoStableDownTop(x, y, self._board._flip(self._color))
                        secondDiagoStable = self.diagoStableTopDown(x, y, self._board._flip(self._color))

                        if horizontalStable and verticalStable and firstDiagoStable and secondDiagoStable:
                            opponnentStability = opponnentStability + 1


        if myStability + opponnentStability is not 0:
            return 100 * (myStability - opponnentStability) / (myStability + opponnentStability)
        else:
            return 0


