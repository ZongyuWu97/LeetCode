class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        last_min = -1
        last_max = -1
        last_out = -1
        prev = [0]*n

        for i in range(n):
            if nums[i] == minK:
                last_min = i
            if nums[i] == maxK:
                last_max = i
            if nums[i] < minK or nums[i] > maxK:
                last_out = i
            prev[i] = [last_min, last_max, last_out]

        dp = [0]*n
        if nums[0] == minK and nums[0] == maxK:
            dp[0] = 1

        for i in range(1, n):
            dp[i] = dp[i-1]
            if minK <= nums[i] <= maxK:
                dp[i] += max(min(prev[i][0], prev[i][1]) - prev[i][2], 0)

        return dp[-1]
