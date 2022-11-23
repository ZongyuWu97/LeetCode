class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(3)]
        dp[0][0] = (1, s[0] == '0', s[0] == '1')
        for i in range(1, n):
            dp[0][i] = (i + 1, dp[0][i - 1][1] + (s[i] == '0'),
                        dp[0][i - 1][2] + (s[i] == '1'))

        for i in range(1, 3):
            base = 1
            for k in range(i):
                if s[k] == s[k + 1]:
                    base = 0
                    break
            dp[i][i] = (base, (s[i] == '0') * base, (s[i] == '1') * base)
            for j in range(i + 1, n):
                dp[i][j] = (dp[i][j - 1][0] + dp[i - 1][j - 1][2] * (s[j] == '0') + dp[i - 1][j - 1][1] * (s[j] == '1'),
                            dp[i][j - 1][1] + dp[i - 1][j][2] * (s[j] == '0'),
                            dp[i][j - 1][2] + dp[i - 1][j][1] * (s[j] == '1'))
        # print(dp)
        return dp[-1][-1][0]
