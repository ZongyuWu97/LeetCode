class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if  n == 2:
            return nums[0] == nums[1]
        dp = [0] * n
        dp[1] = nums[0] == nums[1]
        dp[2] = (nums[0] == nums[1] and nums[1] == nums[2]) or (nums[0] == nums[1] - 1 and nums[1] == nums[2] - 1)
        for i in range(3, n):
            dp[i] = (dp[i - 2] and nums[i] == nums[i - 1])\
                or (dp[i - 3] and nums[i] == nums[i - 1] and nums[i - 1] == nums[i - 2])\
                or (dp[i - 3] and nums[i] == nums[i - 1] + 1 and nums[i - 1] == nums[i - 2] + 1)
        return dp[-1]