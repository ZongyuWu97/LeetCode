class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(3)]

        for k in range(1, 3):
            currMin = prices[0]
            for i in range(k, n):
                currMin = min(currMin, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - currMin)

        return max([x[-1] for x in dp])
