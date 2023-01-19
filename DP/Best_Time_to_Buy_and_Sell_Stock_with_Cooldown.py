class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(2)]
        currMin1 = currMin2 = prices[0]

        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])

            currMin1 = min(currMin1, prices[i] - dp[0][i - 1])
            dp[1][i] = prices[i] - currMin1

            if i >= 2:
                currMin2 = min(currMin2, prices[i] - dp[1][i - 2])
                dp[1][i] = max(dp[1][i], prices[i] - currMin2)

        return max(dp[0][-1], dp[1][-1])
