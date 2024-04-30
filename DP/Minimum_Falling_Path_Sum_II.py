class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = grid[0][i]

        for i in range(1, m):
            minimum = [[dp[i - 1][0], 0], [float("inf"), -1]]
            for j in range(1, n):
                if dp[i - 1][j] < minimum[0][0]:
                    minimum = [[dp[i - 1][j], j], minimum[0]]
                elif dp[i - 1][j] < minimum[1][0]:
                    minimum = [minimum[0], [dp[i - 1][j], j]]
            for j in range(n):
                prev_min = minimum[0][0] if j != minimum[0][1] else minimum[1][0]
                dp[i][j] = prev_min + grid[i][j]
        return min(dp[m - 1])
