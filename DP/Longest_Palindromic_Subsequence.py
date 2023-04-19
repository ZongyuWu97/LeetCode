class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n)]

        # Initialization
        res = 1
        for i in range(n):
            dp[i][i + 1] = 1

        # dp
        for j in range(2, n + 1):
            for i in range(n - j + 1):
                dp[i][i + j] = max(dp[i + 1][i + j - 1] + (s[i] == s[i + j - 1]) * 2,
                                dp[i][i + j - 1], dp[i + 1][i + j])
                res = max(res, dp[i][i + j])
        # print(dp)
        return res