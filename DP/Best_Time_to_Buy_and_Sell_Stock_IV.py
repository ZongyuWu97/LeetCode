class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(k + 1)]

        for transaction in range(1, k + 1):
            currMin = prices[0]
            for i in range(transaction, n):
                currMin = min(currMin, prices[i] - dp[transaction - 1][i - 1])
                dp[transaction][i] = max(
                    dp[transaction][i - 1], prices[i] - currMin)

        return max([x[-1] for x in dp])
