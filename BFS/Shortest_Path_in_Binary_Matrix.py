class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        directions = [(0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1), (1, 1), (1, 0), (1, -1)]
        visited = set([(0, 0)])
        m, n = len(grid), len(grid[0])
        q = deque([(1, 0, 0)])

        while q:
            l, x, y = q.popleft()
            if x == m - 1 and y == n - 1:
                return l
            for dx, dy in directions:
                newX, newY = ｘ + dx, y + dy
                if 0 <= newX < m and 0 <= newY < n:
                    pass
                else:
                    continue
                if (newX, newY) in visited or grid[newX][newY]:
                    continue
                visited.add((newX, newY))
                q.append((l + 1, newX, newY))
        return -1



