class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        memo = [[-1] * (amount + 1) for _ in range(n)]
        def dp(i, amount):
            if amount == 0:
                return 1
            if i == n:
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]

            if coins[i] > amount:
                res = dp(i + 1, amount)
            else:
                res = dp(i, amount - coins[i]) + dp(i + 1, amount)
            memo[i][amount] = res
            return res
        return dp(0, amount)