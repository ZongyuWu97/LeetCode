class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.m, self.n = len(v1), len(v2)
        self.v1, self.v2 = v1, v2
        self.i, self.j = 0, 0
        self.turn = 1

    def next(self) -> int:
        if self.i < self.m and self.j < self.n:
            if self.turn == 1:
                res = self.v1[self.i]
                self.i += 1
            elif self.turn == -1:
                res = self.v2[self.j]
                self.j += 1
            self.turn *= -1
            return res
        else:
            if self.i < self.m:
                res = self.v1[self.i]
                self.i += 1
            else:
                res = self.v2[self.j]
                self.j += 1
            return res

    def hasNext(self) -> bool:
        return self.i < self.m or self.j < self.n


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
