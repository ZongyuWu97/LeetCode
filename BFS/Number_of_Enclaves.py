class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            off_boundary = False
            q = deque([(i, j)])
            count = 1
            while q:
                node = q.popleft()
                for direction in directions:
                    newI, newJ = node[0] + direction[0], node[1] + direction[1]
                    if newI == -1 or newI == m or newJ == -1 or newJ == n:
                        off_boundary = True
                        continue
                    if grid[newI][newJ] != 1:
                        continue
                    grid[newI][newJ] = '.'
                    count += 1
                    q.append((newI, newJ))
            return (not off_boundary) * count


        m, n = len(grid), len(grid[0])
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                grid[i][j] = '.'
                count = bfs(i, j)
                res += count
        return res
