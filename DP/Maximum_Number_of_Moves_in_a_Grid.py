class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        for col in range(n - 2, -1, -1):
            for row in range(m):
                tmp = 0
                for i in range(max(0, row - 1), min(m - 1, row + 1) + 1):
                    if grid[row][col] < grid[i][col + 1] and tmp < dp[i][col + 1] + 1:
                        tmp = dp[i][col + 1] + 1
                dp[row][col] = tmp
                
        return max(dp[i][0] for i in range(m))