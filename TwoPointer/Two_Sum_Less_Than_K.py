class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        res = -1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < k:
                res = max(res, curr_sum)
                left += 1
            else:
                right -= 1
        return res
