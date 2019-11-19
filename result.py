class Result:
    def __init__(self):
        self.w = 0
        self.d = 0
        self.l = 0

    def __str__(self):
        return "w: " + str(self.w) + " l:" + str(self.d) + " d: " + str(self.l)

    def add(self, other):
        self.w += other.w
        self.d += other.d
        self.l += other.l

    def addWin(self):
        self.w += 1

    def addDeuce(self):
        self.d += 1

    def addLose(self):
        self.l += 1

    def toPercent(self):
        result = Result()
        total = self.w + self.d + self.l
        result.w = self.w * 100 / total
        result.d = self.d * 100 / total
        result.l = self.l * 100 / total
        return result
