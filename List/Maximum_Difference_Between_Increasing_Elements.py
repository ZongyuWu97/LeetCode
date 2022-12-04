class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr_min = nums[0]
        max_diff = -1
        for num in nums[1:]:
            if (num - curr_min) > max(0, max_diff):
                max_diff = (num - curr_min)
            curr_min = min(num, curr_min)

        return max_diff
