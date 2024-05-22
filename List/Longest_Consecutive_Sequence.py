class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        res = 1
        n = len(nums)
        curr = 1
        for i in range(1, n):
            if nums[i] - 1 == nums[i - 1]:
                curr += 1
                res = max(res, curr)
            else:
                curr = 1
        return res
