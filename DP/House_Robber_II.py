class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        n = len(self.nums)

        if n <= 3:
            return max(self.nums)

        return max(self.nums[n - 1] + self.robHelper(1, n - 3), self.robHelper(0, n - 2))

    def robHelper(self, i, j) -> int:
        if j == i:
            return self.nums[i]

        dp = [0] * (j - i + 1)

        dp[0], dp[1] = self.nums[i], max(self.nums[i:i + 2])
        for k in range(2, j - i + 1):
            dp[k] = max(self.nums[i + k] + dp[k - 2], dp[k - 1])

        return dp[-1]
