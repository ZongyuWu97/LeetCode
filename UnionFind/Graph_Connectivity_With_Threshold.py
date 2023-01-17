class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        UF = {}

        def find(x):
            if not x in UF:
                UF[x] = x

            if x != UF[x]:
                UF[x] = find(UF[x])

            return UF[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            UF[rootX] = rootY

        def connect(i, j, threshold):
            for num in range(threshold + 1, min(i, j) + 1):
                if i % num == 0 and j % num == 0:
                    return True
            return False

        for num in range(threshold + 1, n + 1):
            mul = 2
            while num * mul <= n:
                union(num, num * mul)
                mul += 1

        res = []
        for a, b in queries:
            res.append(find(a) == find(b))

        return res
