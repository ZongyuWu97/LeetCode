from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def bfs(i, j):
            q = deque([(i, j)])
            while q:
                curr = q.popleft()
                for x, y in directions:
                    newX = curr[0] + x
                    newY = curr[1] + y
                    if 0 <= newX < m and 0 <= newY < n and grid[newX][newY] == "1":
                        grid[newX][newY] = "0"
                        q.append((newX, newY))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    grid[i][j] = "0"
                    bfs(i, j)
        

        return cnt

        