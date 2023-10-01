from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2
        memo = set([(0, 0, k - grid[0][0])]) # row index, columns index, remaining elimination

        q = deque([(0, 0, 0, k - grid[0][0])])
        directinos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            step, row, col, remain = q.popleft()
            if row == m - 1 and col == n - 1:
                return step
            for x, y in directinos:
                newRow, newCol = row + x, col + y
                if 0 <= newRow < m and 0 <= newCol < n:
                    newRemain = remain - grid[newRow][newCol]
                    state = (newRow, newCol, newRemain)
                    if newRemain < 0 or state in memo:
                        continue
                    memo.add(state)
                    q.append((step + 1, newRow, newCol, newRemain))
        return -1


