class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        if n == 1:
            return max(0, (budget >= present[0]) * (future[0] - present[0]))

        dp = [[0] * n for _ in range(budget + 1)]

        for i in range(budget + 1):
            dp[i][0] = (i >= present[0]) * (future[0] >
                                            present[0]) * (future[0] - present[0])

            for j in range(1, n):
                dp[i][j] = dp[i][j - 1]
                if i - present[j] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - present[j]][j - 1] +
                                   (future[j] > present[j]) * (future[j] - present[j]))

        return dp[-1][-1]
