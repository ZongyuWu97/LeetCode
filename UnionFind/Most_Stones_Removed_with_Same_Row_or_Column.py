class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        UF = {}

        def find(x):
            if not x in UF:
                UF[x] = x

            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                UF[rootX] = rootY

        n = len(stones)
        for stone in stones:
            union(stone[0], stone[1] + 10001)

        connect_set = set()
        for idx in UF:
            root = find(idx)
            connect_set.add(root)

        return n - len(connect_set)
