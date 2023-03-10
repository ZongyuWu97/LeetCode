import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        memo = [[False] * n for _ in range(m)]
        h = [(0, 0, 0)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        memo[0][0] = True

        while h:
            time, row, col = heapq.heappop(h)
            if row == m - 1 and col == n - 1:
                return time

            for i, j in direction:
                nrow, ncol = row + i, col + j
                if 0 > nrow or nrow > m - 1 or ncol < 0 or ncol > n - 1 or memo[nrow][ncol]:
                    continue

                memo[nrow][ncol] = True
                wait = (grid[nrow][ncol] - time) % 2 == 0
                heapq.heappush(
                    h, (max(time + 1, grid[nrow][ncol] + wait), nrow, ncol))
