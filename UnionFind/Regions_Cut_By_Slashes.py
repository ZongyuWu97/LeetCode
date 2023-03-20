class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        UF = {}

        def find(x):
            if not x in UF:
                UF[x] = x
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            rootx, rooty = find(x), find(y)
            if rootx != rooty:
                UF[rootx] = rooty

        n = len(grid)
        # 0, 1, 2, 3: north, west, south, east
        for i in range(n):
            for j in range(n):
                # Current node is 4 * i * n + 4 * j
                if grid[i][j] in '/ ':
                    union(4 * i * n + 4 * j + 0, 4 * i * n + 4 * j + 1)
                    union(4 * i * n + 4 * j + 2, 4 * i * n + 4 * j + 3)
                if grid[i][j] in '\ ':
                    union(4 * i * n + 4 * j + 0, 4 * i * n + 4 * j + 3)
                    union(4 * i * n + 4 * j + 1, 4 * i * n + 4 * j + 2)

                # each edge
                if i != 0:
                    union(4 * (i - 1) * n + 4 * j + 2, 4 * i * n + 4 * j + 0)
                if i != n - 1:
                    union(4 * (i + 1) * n + 4 * j + 0, 4 * i * n + 4 * j + 2)
                if j != 0:
                    union(4 * i * n + 4 * (j - 1) + 3, 4 * i * n + 4 * j + 1)
                if j != n - 1:
                    union(4 * i * n + 4 * (j + 1) + 1, 4 * i * n + 4 * j + 3)
        return sum((find(x) == x) for x in range(4 * n * n))
