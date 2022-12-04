class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        n = len(coins)
        tmp = set(coins)

        dp = [[-1] * (amount + 1) for _ in range(n)]
        for i in range(1, amount + 1):
            quotient, remainder = divmod(i, coins[0])
            if remainder == 0:
                dp[0][i] = quotient
            else:
                dp[0][i] = -1
        for i in range(n):
            dp[i][0] = 0

        for i in range(1, n):
            for j in range(1, amount + 1):
                use = -1 if j - coins[i] < 0 else dp[i][j - coins[i]]
                not_use = dp[i - 1][j]
                if use != -1 and not_use != -1:
                    dp[i][j] = min(use + 1, not_use)
                elif use == -1:
                    dp[i][j] = not_use
                else:
                    dp[i][j] = use + 1
        return dp[-1][-1]
                
