class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # find the number of subset < k
        # dp[0] ~ dp[k - 1]
        if sum(nums) < 2 * k:
            return 0
        n = len(nums)
        total = 2 ** n
        MOD = 10 ** 9 + 7
        dp = [[0] * k for _ in range(n + 1)]

        # base case
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, k):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return (total - sum(dp[-1]) * 2) % MOD
