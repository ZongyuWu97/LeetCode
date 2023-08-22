class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        m = [[] for _ in range(n)]
        for start, end, gold in offers:
            m[end].append([start, gold])

        for e in range(1, n + 1):
            dp[e] = dp[e - 1]
            for start, gold in m[e - 1]:
                dp[e] = max(dp[e], dp[start] + gold)
        return dp[-1]