class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        UF = {}
        def find(x):
            if not x in UF:
                UF[x] = x
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                UF[rootX] = rootY

        def unionFind(i, j):
            for direction in directions:
                newX, newY = i + direction[0], j + direction[1]
                if 0 <= newX <= m - 1 and 0 <= newY <= n - 1\
                    and grid[i][j] == grid[newX][newY]:
                    union((i, j), (newX, newY))
        
        # Unionfind all grids
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                unionFind(i, j)

        # Add all islands 
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    islands.add(find((i, j)))
        
        print(islands)
        # Clear not closed islands
        for i in range(m):
            if grid[i][0] == 0 and find((i, 0)) in islands:
                islands.remove(find((i, 0)))
            if grid[i][n - 1] == 0 and find((i, n - 1)) in islands:
                islands.remove(find((i, n - 1)))

        for j in range(n):
            if grid[0][j] == 0 and find((0, j)) in islands:
                islands.remove(find((0, j)))
            if grid[m - 1][j] == 0 and find((m - 1, j)) in islands:
                islands.remove(find((m - 1, j)))

        return len(islands)

