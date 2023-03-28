class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        # dp[i] means cost for days[:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            pass1 = costs[0] + dp[i - 1]
            pass2 = costs[1] + dp[bisect.bisect_left(days, days[i - 1] - 6)]
            pass3 = costs[2] + dp[bisect.bisect_left(days, days[i - 1] - 29)]
            dp[i] = min(pass1, pass2, pass3)
        return dp[-1]