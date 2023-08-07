class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)] # dp[i][j] = strangePrinter(s[i:j + 1])
        for i in range(n):
            dp[i][i] = 1
        for i in range(1, n):
            for j in range(n - i):
                row = j
                col = i + j
                if s[col] == s[col - 1]:
                    dp[row][col] = dp[row][col - 1]
                else:
                    dp[row][col] = dp[row][col - 1] + 1
                    for k in range(row, col - 1):
                        if s[k] == s[col]:
                            dp[row][col] = min(dp[row][col], dp[row][k] + dp[k + 1][col - 1])
        return dp[0][n - 1]
