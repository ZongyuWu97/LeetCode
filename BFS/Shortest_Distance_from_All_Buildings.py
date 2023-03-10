class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = float('inf')
        total = sum([row.count(1) for row in grid])
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    rtn = self.bfs(i, j, grid, m, n, total)
                    if rtn[1] == total:
                        res = min(res, rtn[0])

        return res if res != float('inf') else -1

    def bfs(self, i, j, grid, m, n, total):
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        distance = 0
        now = [(i, j, 0)]
        new = []
        seen = [[0] * n for _ in range(m)]
        cnt = 0

        while now:
            while now:
                row, col, dis = now.pop()
                if grid[row][col] == 1:
                    distance += dis
                    cnt += 1
                    continue

                for x, y in direction:
                    nrow, ncol = row + x, col + y
                    if nrow < 0 or nrow > m - 1 or ncol < 0 or ncol > n - 1\
                            or seen[nrow][ncol] or grid[nrow][ncol] == 2:
                        continue
                    new.append((nrow, ncol, dis + 1))
                    seen[nrow][ncol] = 1

            now, new = new, now

        return distance, cnt
