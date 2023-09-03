class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [['.'] * n for _ in range(m)]
        def dp(m, n):
            if memo[m][n] == '.':
                if m == 0 or n == 0:
                    ans = 1
                else:
                    ans = dp(m - 1, n) + dp(m, n - 1)
                memo[m][n] = ans
            else:
                ans = memo[m][n]
            return ans
        return dp(m - 1, n - 1)