class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        memo = set(nums)
        res = -1
        for num in nums:
            if num > res and -num in memo:
                res = num
        return res
