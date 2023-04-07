class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        left, right = 0, max(nums)
        n = len(nums)

        while left < right:
            mid = (left + right) // 2
            if self.tryMax(nums, mid, n):
                right = mid
            else:
                left = mid + 1
        return left

    
    def tryMax(self, nums, m, n):
        accumulate = 0
        for i in range(n - 1, -1, -1):
            accumulate = max(0, accumulate + nums[i] - m)
        return accumulate <= 0