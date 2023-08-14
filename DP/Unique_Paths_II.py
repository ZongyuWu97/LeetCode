class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = [['.'] * n for _ in range(m)]
        def dp(i, j):
            if memo[i][j] != '.':
                return memo[i][j]
            if i == 0 and j == 0:
                return int(not obstacleGrid[0][0])
            if obstacleGrid[i][j] == 1:
                res = 0
            elif i == 0:
                res = dp(i, j - 1)
            elif j == 0:
                res = dp(i - 1, j)
            else:
                res = dp(i - 1, j) + dp(i, j - 1)
            memo[i][j] = res
            return res
        return dp(m - 1, n - 1)