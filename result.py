class Result:
    def __init__(self):
        self.w = 0
        self.d = 0
        self.l = 0
        self.scores = []
        self.times = []
        self._quickmoves = 0

    def __str__(self):
        value = "w: " + str(self.w) + " d:" + str(self.d) + " l: " + str(self.l)
        (x, y) = self.meanScore()
        value += "\n" + str(x) + " : " + str(y)
        return value

    def add(self, other):
        self.w += other.w
        self.d += other.d
        self.l += other.l
        self.addScores(other)

    def addWin(self):
        self.w += 1

    def addDeuce(self):
        self.d += 1

    def addLose(self):
        self.l += 1

    def resultToPercent(self):
        result = Result()
        total = self.w + self.d + self.l
        result.w = self.w * 100 / total
        result.d = self.d * 100 / total
        result.l = self.l * 100 / total
        return result

    def meanScore(self):
        x = 0
        y = 0
        for s in self.scores:
            x += s[0]
            y += s[1]
        return x / len(self.scores), y / len(self.scores)

    def addScore(self, a, b):
        self.scores.append((a, b))

    def meanTime(self):
        result = 0
        for t in self.times:
            result += t
        return result / len(self.scores)

    def addTime(self, a, b):
        self.times.append((a, b))

    def reverse(self):
        r = Result()
        r.w = self.l
        r.l = self.w
        r.d = self.d
        for s in self.scores:
            r.addScore(s[1], s[0])
        return r

    def addScores(self, other):
        for s in other.scores:
            self.addScore(s[0], s[1])
        pass
