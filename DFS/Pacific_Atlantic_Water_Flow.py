class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        both = [[0] * n for _ in range(m)]
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(visited, x, y):
            if (x, y) in visited:
                return
            else:
                visited.add((x, y))
            both[x][y] += 1
            for d in directions:
                newX, newY = x + d[0], y + d[1]
                if (
                    0 <= newX < m
                    and 0 <= newY < n
                    and heights[newX][newY] >= heights[x][y]
                ):
                    dfs(visited, newX, newY)

        for i in range(m):
            dfs(visited, i, 0)
        for j in range(n):
            dfs(visited, 0, j)

        visited = set()
        for i in range(m):
            dfs(visited, i, n - 1)
        for j in range(n):
            dfs(visited, m - 1, j)

        res = []
        for i in range(m):
            for j in range(n):
                if both[i][j] == 2:
                    res.append([i, j])

        return res
