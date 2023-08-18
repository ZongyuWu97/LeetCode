from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        memo = [['.'] * n for _ in range(m)]
        visited = set()
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    memo[i][j] = 0
                    q.append((i, j, 0))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            row, col, distance = q.popleft()
            for x, y in directions:
                newRow, newCol = row + x, col + y
                if 0 <= newRow < m and 0 <= newCol < n and memo[newRow][newCol] == '.':
                    memo[newRow][newCol] = distance + 1
                    q.append((newRow, newCol, distance + 1))

        return memo
